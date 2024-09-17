from rest_framework import serializers

from apps.features.models import Feature, FeatureValue, DiscountFeature


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = '__all__'


class FeatureValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureValue
        fields = '__all__'


class DiscountFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountFeature
        fields = '__all__'
