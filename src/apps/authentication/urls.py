from django.urls import path

from apps.authentication import views


urlpatterns = [
    path('forgot-password/', views.ForgotPasswordAPIView.as_view(), name='forgot-password'),
    path('forgot-password/new_password/', views.NewPasswordAPIView.as_view(), name='new_password'),

    path('register/send_code/', views.SendCodeAPIView.as_view(), name='send_code'),
    path('register/verify_code/', views.VerifyCodeAPIView.as_view(), name='verify_code'),
    path('register/', views.RegisterAPIView.as_view(), name='register'),
]
