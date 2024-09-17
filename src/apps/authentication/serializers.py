import random

from django.core.cache import cache
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers

from rest_framework_simplejwt.tokens import RefreshToken

from apps.authentication.sms_providers import EskizUz
from apps.users.validators import validate_phone_number


class ForgotPasswordSerializer(serializers.Serializer):
    phone_number = serializers.CharField(validators=[validate_phone_number])
    link = serializers.CharField(read_only=True)

    def validate_phone_number(self, phone_number):
        if not get_user_model().objects.filter(phone_number=phone_number).exists():
            raise ValidationError("User with this phone number does not exist.")
        return phone_number

    def save(self, *args, **kwargs):
        """
        Send forgot password link to phone number user.
        """
        forgot_id = random.randint(1000, 9999)
        link = self.context['request'].build_absolute_uri(f'new_password/?forgot_id={forgot_id}')
        EskizUz.send_sms(
            send_type='FORGOT_PASSWORD',
            phone_number=self.validated_data['phone_number'],
            link=link
        )

        self.validated_data['link'] = link

        cache.set(f'forgot_id={forgot_id}', self.validated_data['phone_number'], timeout=60 * 10)


class NewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(validators=[validate_password], write_only=True)
    refresh = serializers.CharField(read_only=True)
    access = serializers.CharField(read_only=True)

    def save(self, **kwargs):
        attrs = self.validated_data
        context = self.context

        phone_number, forgot_id = context['phone_number'], context['forgot_id']

        user = get_user_model().objects.get(phone_number=phone_number)
        user.set_password(attrs['password'])
        user.save()

        cache.delete(f'forgot_id={forgot_id}')

        refresh = RefreshToken.for_user(user)
        attrs['refresh'] = str(refresh)
        attrs['access'] = str(refresh.access_token)


class SendCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField(validators=[validate_phone_number])

    def validate_phone_number(self, phone_number):
        if get_user_model().objects.filter(phone_number=phone_number).exists():
            raise ValidationError("User with this phone number already exists.")
        return phone_number

    def save(self, *args, **kwargs):
        """
        Send registration code to phone number user.
        """

        code = EskizUz.send_sms(
            send_type='AUTH_CODE',
            phone_number=self.validated_data['phone_number'],
        )

        self.validated_data['code'] = code


class VerifyCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13, min_length=13, validators=[validate_phone_number], write_only=True)
    code = serializers.IntegerField(write_only=True)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        phone_number, code = attrs['phone_number'], attrs['code']

        if cache.get(f'auth_code_{phone_number}') != code:
            raise serializers.ValidationError('Неверный номер телефона или код')

        return attrs


class RegisterSerializer(VerifyCodeSerializer):
    password = serializers.CharField(max_length=128, validators=[validate_password], write_only=True)
    refresh = serializers.CharField(read_only=True)
    access = serializers.CharField(read_only=True)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        phone_number, password = attrs['phone_number'], attrs['password']

        user = get_user_model().objects.create_user(phone_number=phone_number, password=password)

        cache.delete(f'{phone_number}_auth_code')

        refresh = RefreshToken.for_user(user)
        attrs['refresh'] = str(refresh)
        attrs['access'] = str(refresh.access_token)

        return attrs
