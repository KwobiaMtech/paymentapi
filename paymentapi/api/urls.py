from django.urls import path

from .views import PaymentRequestAPIView, SubmitPhoneAPIView, SubmitPinAPIView, SubmitOTPAPIView

app_name = "charge"

urlpatterns = [
    path('', PaymentRequestAPIView.as_view(), name="pay"),
    path('submit_pin', SubmitPinAPIView.as_view(), name="submit_pin"),
    path('submit_phone', SubmitPhoneAPIView.as_view(), name="submit_phone"),
    path('submit_otp', SubmitOTPAPIView.as_view(), name="submit_otp")
]
