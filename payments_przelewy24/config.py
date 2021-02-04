from __future__ import annotations

import hashlib
import json
import os
from dataclasses import dataclass

PRODUCTION_URL: str = "https://secure.przelewy24.pl/"
SANDBOX_URL: str = "https://sandbox.przelewy24.pl/"
P24_TEST_CONNECTION: str = "api/v1/testAccess"
P24_TRANSACTION_REQUEST: str = "trnRequest"
P24_TRANSACTION_REGISTER: str = "api/v1/transaction/register"
P24_TRANSACTION_VERIFY: str = "api/v1/transaction/verify"


@dataclass
class Endpoints:
    testConnection: str
    transactionRequest: str
    transactionRegister: str
    transactionVerify: str


@dataclass(init=False)
class Przelewy24Config:

    pos_id: int
    merchant_id: int
    crc: str
    api_key: str
    endpoints: Endpoints

    def __init__(
        self, pos_id: int, merchant_id: int, crc: str, api_key: str, sandbox: bool
    ):
        self.pos_id = pos_id
        self.merchant_id = merchant_id
        self.crc = crc
        self.api_key = api_key
        base_url = SANDBOX_URL if sandbox else PRODUCTION_URL
        self.endpoints = Endpoints(
            testConnection=f"{base_url}{P24_TEST_CONNECTION}",
            transactionRequest=f"{base_url}{P24_TRANSACTION_REQUEST}",
            transactionRegister=f"{base_url}{P24_TRANSACTION_REGISTER}",
            transactionVerify=f"{base_url}{P24_TRANSACTION_VERIFY}",
        )

    def generate_sign(self, **kwargs) -> str:
        return hashlib.sha384(
            json.dumps({**kwargs, **{"crc": self.crc}}).replace(" ", "").encode("utf-8")
        ).hexdigest()

    @classmethod
    def from_env(cls, prefix: str = "PAYMENTS_") -> Przelewy24Config:
        return cls(
            pos_id=int(os.getenv(f"{prefix}P24_POS_ID", 0)),
            merchant_id=int(os.getenv(f"{prefix}P24_MERCHANT_ID", 0)),
            crc=os.getenv(f"{prefix}P24_CRC", "provide P24 CRC"),
            api_key=os.getenv(f"{prefix}P24_API_KEY", "provide P24 API KEY"),
            sandbox=bool(int(os.getenv(f"{prefix}P24_SANDBOX", "1")) != "0"),
        )
