
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from apps.features.models import FeatureValue
from apps.features.serializers import FeatureValueSerializer

"""
View to do CRUD operations on Feature Value. Only admins can do it.
"""



# api view to create feature values
class FeatureValueCreateAPIView(generics.CreateAPIView):
    queryset = FeatureValue.objects.all()
    serializer_class = FeatureValueSerializer
    permission_classes = (IsAdminUser,)


# api view to see singular feature value with specific id
class FeatureValueRetrieveAPIView(generics.RetrieveAPIView):
    queryset = FeatureValue.objects.all()
    serializer_class = FeatureValueSerializer
    permission_classes = (IsAdminUser,)


# api view to update feature values
class FeatureValueUpdateAPIView(generics.UpdateAPIView):
    queryset = FeatureValue.objects.all()
    serializer_class = FeatureValueSerializer
    permission_classes = (IsAdminUser,)


# api view to delete feature values
class FeatureValueDeleteAPIView(generics.DestroyAPIView):
    queryset = FeatureValue.objects.all()
    serializer_class = FeatureValueSerializer
    permission_classes = (IsAdminUser,)


# api view to see all the feature values
class FeatureValueListAPIView(generics.ListAPIView):
    queryset = FeatureValue.objects.all()
    serializer_class = FeatureValueSerializer
    permission_classes = (IsAdminUser,)