from django.urls import path

from .views import discounts, discount_images, discount_services

urlpatterns = [
    # discounts
    path('/', discounts.DiscountListAPIView.as_view(), name='discounts-list'),
    path('discounts/create/', discounts.DiscountCreateAPIView.as_view(), name='discounts-create'),
    path('discounts/<int:pk>/', discounts.DiscountRetrieveAPIView.as_view(), name='discounts-detail'),
    path('discounts/update/<int:pk>/', discounts.DiscountUpdateAPIView.as_view(), name='discounts-update'),
    path('discounts/delete/<int:pk>/', discounts.DiscountDeleteAPIView.as_view(), name='discounts-delete'),

    # discount images
    path('discount-images/', discount_images.DiscountImageListAPIView.as_view(),
         name='discount-images-list'),

    path('discount-images/create/', discount_images.DiscountImageCreateAPIView.as_view(),
         name='discount-images-create'),

    path('discount-images/<int:pk>/', discount_images.DiscountImageRetrieveAPIView.as_view(),
         name='discount-images-detail'),

    path('discount-images/update/<int:pk>/', discount_images.DiscountImageUpdateAPIView.as_view(),
         name='discount-images-update'),

    path('discount-images/delete/<int:pk>/', discount_images.DiscountImageDeleteAPIView.as_view(),
         name='discount-images-delete'),

    # discount services
    path('discount-services/', discount_services.DiscountServiceListAPIView.as_view(),
         name='discount-services-list'),

    path('discount-services/create/', discount_services.DiscountServiceCreateAPIView.as_view(),
         name='discount-services-create'),

    path('discount-services/<int:pk>/', discount_services.DiscountServiceRetrieveAPIView.as_view(),
         name='discount-services-detail'),

    path('discount-services/update/<int:pk>/', discount_services.DiscountServiceUpdateAPIView.as_view(),
         name='discount-services-update'),

    path('discount-services/delete/<int:pk>/', discount_services.DiscountServiceDeleteAPIView.as_view(),
         name='discount-services-delete'),
]
