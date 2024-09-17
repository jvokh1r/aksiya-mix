
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from apps.discounts.models import Discount
from apps.discounts.serializers import DiscountSerializer

"""
View to do CRUD operations on Discounts. Only company owners can do it.
"""


# api view to create discounts
class DiscountCreateAPIView(generics.CreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    permission_classes = (IsAdminUser,)


# api view to see singular discount with specific id
class DiscountRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    permission_classes = (IsAdminUser,)


# api view to update discounts
class DiscountUpdateAPIView(generics.UpdateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    permission_classes = (IsAdminUser,)


# api view to delete discounts
class DiscountDeleteAPIView(generics.DestroyAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    permission_classes = (IsAdminUser,)


# api view to see all the discounts
class DiscountListAPIView(generics.ListAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    permission_classes = (IsAdminUser,)