
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from apps.discounts.models import DiscountService
from apps.discounts.serializers import DiscountServiceSerializer

"""
View to do CRUD operations on Discount Services. Only company owners can do it.
"""


# api view to create discount services
class DiscountServiceCreateAPIView(generics.CreateAPIView):
    queryset = DiscountService.objects.all()
    serializer_class = DiscountServiceSerializer
    permission_classes = (IsAdminUser,)


# api view to see singular discount service with specific id
class DiscountServiceRetrieveAPIView(generics.RetrieveAPIView):
    queryset = DiscountService.objects.all()
    serializer_class = DiscountServiceSerializer
    permission_classes = (IsAdminUser,)


# api view to update discount services
class DiscountServiceUpdateAPIView(generics.UpdateAPIView):
    queryset = DiscountService.objects.all()
    serializer_class = DiscountServiceSerializer
    permission_classes = (IsAdminUser,)


# api view to delete discount services
class DiscountServiceDeleteAPIView(generics.DestroyAPIView):
    queryset = DiscountService.objects.all()
    serializer_class = DiscountServiceSerializer
    permission_classes = (IsAdminUser,)


# api view to see all the discount services
class DiscountServiceListAPIView(generics.ListAPIView):
    queryset = DiscountService.objects.all()
    serializer_class = DiscountServiceSerializer
    permission_classes = (IsAdminUser,)