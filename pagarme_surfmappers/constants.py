# -*- coding: utf-8 -*-
BASE_URL = "https://api.pagar.me/1/"
# Transaction's URLs:
CREATE_TRANSACTION_URL = BASE_URL + "transactions"
CAPTURE_TRANSACTION_URL = BASE_URL + "transactions/{0}/capture"
# Bank's URLs:
CREATE_BANK_URL = BASE_URL + "bank_accounts"
GET_BANK_URL = BASE_URL + "bank_accounts/{0}"
