import json
import logging
from decimal import Decimal

import pytest
import responses
from payments import get_payment_model
from payments.models import BasePayment

from payments_przelewy24.api import Przelewy24API, Transaction
from payments_przelewy24.config import Przelewy24Config
from payments_przelewy24.provider import Przelewy24Provider

logging.basicConfig(level=logging.DEBUG, format="%(name)s %(levelname)s %(message)s")


@pytest.fixture
def config() -> Przelewy24Config:
    return Przelewy24Config.from_env()


@pytest.fixture
def response(config: Przelewy24Config):
    with responses.RequestsMock() as resp:
        yield {
            config.endpoints.testConnection: {
                200: lambda: resp.add(
                    responses.GET,
                    config.endpoints.testConnection,
                    body=json.dumps(dict(data=True, error="")),
                    status=200,
                ),
                400: lambda: resp.add(
                    responses.GET,
                    config.endpoints.testConnection,
                    body=json.dumps(dict(code=400, error="Invalid input data")),
                    status=400,
                ),
            },
            config.endpoints.transactionRegister: {
                200: lambda: resp.add(
                    responses.POST,
                    config.endpoints.transactionRegister,
                    body=json.dumps(
                        dict(data=dict(token="1234-123-12"), responseCode="200")
                    ),
                    status=200,
                ),
                400: lambda: resp.add(
                    responses.POST,
                    config.endpoints.transactionRegister,
                    body=json.dumps(dict(code=400, error="Invalid input data")),
                    status=400,
                ),
            },
        }


@pytest.fixture
def api(config):
    return Przelewy24API(config)


@pytest.fixture
def transaction() -> Transaction:
    return Transaction(
        amount=100,
        sessionId="123",
        currency="PLN",
        description="Test",
        email="foo@bar.com",
        country="PL",
        language="pl",
    )


@pytest.fixture
def provider(config: Przelewy24Config) -> Przelewy24Provider:
    return Przelewy24Provider(config=config)


@pytest.fixture
def payment(db) -> BasePayment:
    Payment = get_payment_model()
    return Payment.objects.create(
        variant="przelewy24",  # this is the variant from PAYMENT_VARIANTS
        description="Book purchase",
        total=Decimal(120.24),
        tax=Decimal(20),
        currency="PLN",
        delivery=Decimal(10),
        billing_first_name="Sherlock",
        billing_last_name="Holmes",
        billing_address_1="221B Baker Street",
        billing_address_2="",
        billing_city="London",
        billing_postcode="NW1 6XE",
        billing_country_code="GB",
        billing_country_area="Greater London",
        customer_ip_address="127.0.0.1",
    )


@pytest.fixture
def correct_process_data(config: Przelewy24Config, payment: BasePayment):
    common = {
        "merchantId": 104748,
        "posId": 104748,
        "sessionId": str(payment.pk),
        "amount": 12024,
        "originAmount": 12024,
        "currency": "PLN",
        "orderId": 306026561,
        "methodId": 154,
        "statement": "p24-G02-A65-G61",
    }
    return {**common, **{"sign": config.generate_sign(**common)}}
