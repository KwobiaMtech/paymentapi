from rest_framework import status, permissions
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .serializers import PaymentRequestSerializer, TransactionResponseSerializer, SubmitPinSerializer, \
    SubmitOTPSerializer, SubmitPhoneSerializer
from .DataModel.PayStackApi import PayStack


class PaymentRequestAPIView(CreateAPIView):
    serializer_class = PaymentRequestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        data = serializer.data
        del data['user']
        paystack = PayStack(data)
        paystack.initiate_payment()

        transaction_serializer = TransactionResponseSerializer(data=paystack.user_response)
        transaction_serializer.is_valid(raise_exception=True)
        transaction_serializer.save(user=self.request.user)

        return Response(paystack.user_response, status=status.HTTP_201_CREATED)


class SubmitPinAPIView(CreateAPIView):
    serializer_class = SubmitPinSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(PayStack.chargeValidation('submit_pin', serializer.data))


class SubmitOTPAPIView(CreateAPIView):
    serializer_class = SubmitOTPSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(PayStack.chargeValidation('submit_otp', serializer.data))


class SubmitPhoneAPIView(CreateAPIView):
    serializer_class = SubmitPhoneSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(PayStack.chargeValidation('submit_phone', serializer.data))
