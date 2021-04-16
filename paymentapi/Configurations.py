from dataclasses import dataclass
import os

# Initialise environment variables
import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
environ.Env.read_env()


@dataclass
class Configuration:
    def __init__(self):
        pass

    DEBUG: str = os.environ.get('DEBUG')
    PAYSTACK_SECRET_KEY: str = os.environ.get('PAYSTACK_SECRET_KEY_TEST') if DEBUG is False else os.environ.get('PAYSTACK_SECRET_KEY_LIVE')
    PAYSTACK_PUBLIC_KEY: str = os.environ.get('PAYSTACK_PUBLIC_KEY_TEST') if DEBUG is False else os.environ.get('PAYSTACK_PUBLIC_KEY_LIVE')
    PAYSTACK_API: str = os.environ.get('PAYSTACK_API')
    PAYSTACK_API_REF: str = "https://api.paystack.co/transaction/verify/"
