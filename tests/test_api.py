import pytest

from payments_przelewy24.api import Przelewy24API, Transaction
from payments_przelewy24.config import Przelewy24Config


def test_test_connection_should_pass(config: Przelewy24Config, api, response):
    response[config.endpoints.testConnection][200]()
    assert api.testConnection()


def test_test_connection_should_not_pass(config: Przelewy24Config, api, response):
    response[config.endpoints.testConnection][400]()
    with pytest.raises(RuntimeError):
        api.testConnection()


def test_register_should_pass(
    config: Przelewy24Config, api: Przelewy24API, transaction: Transaction, response
):
    response[config.endpoints.transactionRegister][200]()
    api.register(
        transaction=transaction,
        success_url="https://przelewy24.source.net.pl/payments/przelewy24",
        status_url="https://przelewy24.source.net.pl/payments/przelewy24/status",
    )


@pytest.mark.live
def test_live_test_connection_should_pass(api):
    assert api.testConnection()


@pytest.mark.live
def test_live_test_connection_should_register_transaction(
    api: Przelewy24API, transaction: Transaction
):
    assert api.register(
        transaction=transaction,
        success_url="https://przelewy24.source.net.pl/payments/przelewy24",
        status_url="https://przelewy24.source.net.pl/payments/przelewy24/status",
    )
