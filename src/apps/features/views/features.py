from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from apps.features.models import Feature
from apps.features.serializers import FeatureSerializer


"""
View to do CRUD operations on Features. Only admins can do it.
"""


# api view to create features
class FeatureCreateAPIView(generics.CreateAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    permission_classes = (IsAdminUser,)


# api view to see singular feature with specific id
class FeatureRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    permission_classes = (IsAdminUser,)


# api view to update features
class FeatureUpdateAPIView(generics.UpdateAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    permission_classes = (IsAdminUser,)


# api view to delete features
class FeatureDeleteAPIView(generics.DestroyAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    permission_classes = (IsAdminUser,)


# api view to see all the features
class FeatureListAPIView(generics.ListAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    permission_classes = (IsAdminUser,)