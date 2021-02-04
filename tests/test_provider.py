import logging

import pytest

from payments_przelewy24.api import Przelewy24API, Transaction
from payments_przelewy24.config import Przelewy24Config
from payments_przelewy24.forms import ProcessForm

logging.basicConfig(level=logging.DEBUG, format="%(name)s %(levelname)s %(message)s")


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
        success_url="https://www.source.net.pl/payments/przelewy24",
        status_url="https://www.source.net.pl/payments/przelewy24/status",
    )


def test_process_form(correct_process_data, payment, config: Przelewy24Config):
    form = ProcessForm(payment=payment, config=config, data=correct_process_data)
    assert form.is_valid()
    assert len(form.errors) == 0
