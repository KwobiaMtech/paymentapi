from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import UserRequest, TransactionResponse


def provider_choices():
    return ['mtn', 'vod', 'tgo']


class PaymentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "date_joined")


class PaymentRequestSerializer(serializers.ModelSerializer):
    user = PaymentUserSerializer(read_only=True)
    provider = serializers.ChoiceField(provider_choices())

    class Meta:
        model = UserRequest
        fields = ("user", "amount", "email", "reference", "phone", "provider", "callback_url")


class TransactionResponseSerializer(serializers.ModelSerializer):
    user = PaymentUserSerializer(read_only=True)

    class Meta:
        model = TransactionResponse
        fields = ("user", "reference", "status", "message", "display_text")


class SubmitPinSerializer(serializers.Serializer):
    pin = serializers.CharField(max_length=200)
    reference = serializers.CharField(max_length=200)


class SubmitOTPSerializer(serializers.Serializer):
    otp = serializers.CharField(max_length=200)
    reference = serializers.CharField(max_length=200)


class SubmitPhoneSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=200)
    reference = serializers.CharField(max_length=200)
