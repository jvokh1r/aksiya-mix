
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from apps.features.models import DiscountFeature
from apps.features.serializers import DiscountFeatureSerializer

"""
View to do CRUD operations on Discount Feature. Only admins can do it.
"""


# api view to create discount feature
class DiscountFeatureCreateAPIView(generics.CreateAPIView):
    queryset = DiscountFeature.objects.all()
    serializer_class = DiscountFeatureSerializer
    permission_classes = (IsAdminUser,)


# api view to see singular discount feature with specific id
class DiscountFeatureRetrieveAPIView(generics.RetrieveAPIView):
    queryset = DiscountFeature.objects.all()
    serializer_class = DiscountFeatureSerializer
    permission_classes = (IsAdminUser,)


# api view to update discount features
class DiscountFeatureUpdateAPIView(generics.UpdateAPIView):
    queryset = DiscountFeature.objects.all()
    serializer_class = DiscountFeatureSerializer
    permission_classes = (IsAdminUser,)


# api view to delete discount features
class DiscountFeatureDeleteAPIView(generics.DestroyAPIView):
    queryset = DiscountFeature.objects.all()
    serializer_class = DiscountFeatureSerializer
    permission_classes = (IsAdminUser,)


# api view to see all the discount features
class DiscountFeatureListAPIView(generics.ListAPIView):
    queryset = DiscountFeature.objects.all()
    serializer_class = DiscountFeatureSerializer
    permission_classes = (IsAdminUser,)