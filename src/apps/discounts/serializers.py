from rest_framework import serializers

from apps.discounts.models import Discount, DiscountImage, DiscountService


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'


class DiscountImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountImage
        fields = '__all__'


class DiscountServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountService
        fields = '__all__'
