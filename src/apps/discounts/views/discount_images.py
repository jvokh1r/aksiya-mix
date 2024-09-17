
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from apps.discounts.models import DiscountImage
from apps.discounts.serializers import DiscountImageSerializer

"""
View to do CRUD operations on Discount Images. Only company owners can do it.
"""


# api view to create discounts
class DiscountImageCreateAPIView(generics.CreateAPIView):
    queryset = DiscountImage.objects.all()
    serializer_class = DiscountImageSerializer
    permission_classes = (IsAdminUser,)


# api view to see singular discount with specific id
class DiscountImageRetrieveAPIView(generics.RetrieveAPIView):
    queryset = DiscountImage.objects.all()
    serializer_class = DiscountImageSerializer
    permission_classes = (IsAdminUser,)


# api view to update discounts
class DiscountImageUpdateAPIView(generics.UpdateAPIView):
    queryset = DiscountImage.objects.all()
    serializer_class = DiscountImageSerializer
    permission_classes = (IsAdminUser,)


# api view to delete discounts
class DiscountImageDeleteAPIView(generics.DestroyAPIView):
    queryset = DiscountImage.objects.all()
    serializer_class = DiscountImageSerializer
    permission_classes = (IsAdminUser,)


# api view to see all the discounts
class DiscountImageListAPIView(generics.ListAPIView):
    queryset = DiscountImage.objects.all()
    serializer_class = DiscountImageSerializer
    permission_classes = (IsAdminUser,)