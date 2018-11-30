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
CREATE_BULK_ANTICIPATION_URL = "recipients/{0}/bulk_anticipations"
GET_BULK_LIMITS = "recipients/{0}/bulk_anticipations/limits"
CONFIRM_BULK_ANTICIPATION = "{0}/bulk_anticipations/{1}/confirm"
CANCEL_BULK_ANTICIPATION = "recipients/{0}/bulk_anticipations/{1}/cancel"
# Transfer's URLs:
CREATE_TRANSFER_URL = BASE_URL + "transfers"
GET_TRANSFER_URL = BASE_URL + "transfers/{0}"
CANCEL_TRANSFER_URL = BASE_URL + "transfers/{0}/cancel"
