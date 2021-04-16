import requests
from ..DataModel.PayStackApi import PayStack
# from api.DataModel.PayStackApi import PayStack
from ..models import TransactionResponse as model, UserRequest as request_model
from ..serializers import TransactionResponseSerializer, PaymentRequestSerializer


class PayRepository:

    @staticmethod
    def updateAllTransactions():
        transactions = model.objects.filter(transaction_status="pending")
        serializer = TransactionResponseSerializer(transactions, many=True)
        for item in serializer.data:
            status_response = PayStack.checkStatus(item["reference"])
            callback_status = PayRepository.sendCallBack(status_response)
            if callback_status:
                PayRepository.updateReferenceTransaction(
                    status_response["reference"],
                    status_response["status"],
                    callback_status
                )

    @staticmethod
    def updateReferenceTransaction(ref, status, callback_status):
        transactions = model.objects.get(reference=ref)
        transactions.transaction_status = status
        transactions.callback_status = callback_status
        transactions.save()

    @staticmethod
    def sendCallBack(data):
        callback_data = request_model.objects.filter(reference=data['reference']).first()
        try:
            if callback_data:
                response = requests.post(callback_data.callback_url, data=data)
                return response.status_code
            return "failed"
        except:
            return "failed"
