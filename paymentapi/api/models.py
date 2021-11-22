from enum import Enum

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class UserRequest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.CharField(_("Amount"), max_length=255)
    email = models.CharField(_("Email"), max_length=255)
    reference = models.CharField(_("Reference"), max_length=255, unique=True)
    phone = models.CharField(_("Phone Number"), max_length=255)

    class Providers(models.TextChoices):
        MTN = 'mtn'
        Vodafone = 'vod'
        AirtelTigo = 'tgo'

    provider = models.CharField(
        max_length=255,
        choices=Providers.choices,
        null=True
    )
    callback_url = models.CharField(_("Callback Url"), max_length=255)
    date_created = models.DateTimeField(_("Date Created"), auto_now_add=True, null=True)


class TransactionResponse(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reference = models.CharField(_("Reference"), max_length=255)
    status = models.CharField(_("Status"), max_length=255)
    message = models.CharField(_("Message"), max_length=255, null=True)
    display_text = models.CharField(_("Display Text"), max_length=255, null=True, default="")
    transaction_status = models.CharField(_("Transaction Status"), max_length=255, default="pending", null=True)
    callback_status = models.CharField(_("Call Back Status"), max_length=255,null=True)
