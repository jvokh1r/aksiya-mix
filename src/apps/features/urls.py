from django.urls import path

from .views import features, feature_values, discount_features

urlpatterns = [
    # features
    path('/', features.FeatureListAPIView.as_view(), name='features-list'),
    path('features/create/', features.FeatureCreateAPIView.as_view(), name='features-create'),
    path('features/<int:pk>/', features.FeatureRetrieveAPIView.as_view(), name='features-detail'),
    path('features/update/<int:pk>/', features.FeatureUpdateAPIView.as_view(), name='features-update'),
    path('features/delete/<int:pk>/', features.FeatureDeleteAPIView.as_view(), name='features-delete'),

    # feature values
    path('feature-values/', feature_values.FeatureValueListAPIView.as_view(),
         name='feature-values-list'),

    path('feature-values/create/', feature_values.FeatureValueCreateAPIView.as_view(),
         name='feature-values-create'),

    path('feature-values/<int:pk>/', feature_values.FeatureValueRetrieveAPIView.as_view(),
         name='feature-values-detail'),

    path('feature-values/update/<int:pk>/', feature_values.FeatureValueUpdateAPIView.as_view(),
         name='feature-values-update'),

    path('feature-values/delete/<int:pk>/', feature_values.FeatureValueDeleteAPIView.as_view(),
         name='feature-values-delete'),

    # discount feature
    path('discount-features/', discount_features.DiscountFeatureListAPIView.as_view(),
         name='discount-features-list'),

    path('discount-features/create/', discount_features.DiscountFeatureCreateAPIView.as_view(),
         name='discount-features-create'),

    path('discount-features/<int:pk>/', discount_features.DiscountFeatureRetrieveAPIView.as_view(),
         name='discount-features-detail'),

    path('discount-features/update/<int:pk>/', discount_features.DiscountFeatureUpdateAPIView.as_view(),
         name='discount-features-update'),

    path('discount-features/delete/<int:pk>/', discount_features.DiscountFeatureDeleteAPIView.as_view(),
         name='discount-features-delete'),
]
