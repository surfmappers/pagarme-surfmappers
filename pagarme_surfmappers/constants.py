# -*- coding: utf-8 -*-
BASE_URL = "https://api.pagar.me/1/"
# Transaction's URLs:
CREATE_TRANSACTION_URL = BASE_URL + "transactions"
CAPTURE_TRANSACTION_URL = BASE_URL + "transactions/{0}/capture"
# Bank's URLs:
CREATE_BANK_URL = BASE_URL + "bank_accounts"
GET_BANK_URL = BASE_URL + "bank_accounts/{0}"
# Recipient's URLs:
CREATE_RECIPIENT_URL = BASE_URL + "recipients"
GET_RECIPIENT_URL = BASE_URL + "recipients/{0}"
GET_RECIPIENT_BALANCE_URL = BASE_URL + "recipients/{0}/balance"
