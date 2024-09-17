from django.core.cache import cache

from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, GenericAPIView

from apps.authentication.serializers import (ForgotPasswordSerializer, RegisterSerializer, SendCodeSerializer,
                                             VerifyCodeSerializer, NewPasswordSerializer)


class ForgotPasswordAPIView(CreateAPIView):
    """
    This view is used to send a forgot password phone number to the user.
    """
    permission_classes = ()
    authentication_classes = ()

    serializer_class = ForgotPasswordSerializer


class NewPasswordAPIView(GenericAPIView):
    permission_classes = ()
    authentication_classes = ()

    serializer_class = NewPasswordSerializer

    def post(self, request, *args, **kwargs):
        forgot_id = request.GET.get('forgot_id', None)
        phone_number = cache.get(f'forgot_id={forgot_id}', None)
        if not phone_number:
            return Response({'message': 'Invalid path'}, status=404)
        serializer = self.get_serializer(data=request.data,
                                         context={'phone_number': phone_number,
                                                  'forgot_id': forgot_id, })
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)


class SendCodeAPIView(GenericAPIView):
    """
    View to send code.
    """
    permission_classes = ()
    authentication_classes = ()

    serializer_class = SendCodeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=200)


class VerifyCodeAPIView(GenericAPIView):
    """
    View to verify code.
    """

    permission_classes = ()
    authentication_classes = ()

    serializer_class = VerifyCodeSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=200)


class RegisterAPIView(GenericAPIView):
    """
    View to register a new user.
    """

    permission_classes = ()
    authentication_classes = ()

    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=200)
