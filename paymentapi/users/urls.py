from django.urls import path
from .views import UserRegistrationAPIView, UserLoginAPIView, UserTokenAPIView

app_name = 'users'

urlpatterns = [
    path('users/', UserRegistrationAPIView.as_view(), name="create_user"),
    path('users/login/', UserLoginAPIView.as_view(), name="login"),
    path('tokens/<key>', UserTokenAPIView.as_view(), name="token")
]
