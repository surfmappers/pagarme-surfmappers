# Pagarme Surfmappers
[![Latest PyPI version](https://img.shields.io/pypi/v/pagarme-surfmappers.svg)](https://pypi.python.org/pypi/pagarme-surfmappers/) [![Wheel Status](https://img.shields.io/pypi/wheel/pagarme-surfmappers.svg)](https://pypi.python.org/pypi/pagarme-surfmappers/) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/pagarme-surfmappers.svg)](https://pypi.python.org/pypi/pagarme-surfmappers/) [![License](https://img.shields.io/pypi/l/pagarme-surfmappers.svg)](https://pypi.python.org/pypi/pagarme-surfmappers/)

An implementation of the Pagar.me API for Python. This repository appears as an alternative to the Pagar.me library suggested by the documentation, that has some problems and which, for example, was not used by us because of this.

# Install

```pip install pagarme-surfmappers```

# How to use
You can use this lib as [Pagar.me documentation](https://docs.pagar.me/v2017-08-28/reference) suggests to. Above we'll show some examples

We gonna assume that you already have an valid Pagar.me api key:

```python
YOUR_API_KEY = "your_pagarme_api_key"
```

## Summary


## Bank Account
You can create and get an bank account. Check [Pagar.me documentation](https://docs.pagar.me/v2017-08-28/reference#criando-uma-conta-banc%C3%A1ria) for more details:

### Create Bank Account
```python
import pagarme_surfmappers

YOUR_API_KEY = "your_pagarme_api_key"

pagarme_surfmappers.set_api_key(YOUR_API_KEY)
bank_account = pagarme_surfmappers.BankAccount()

params = {
    ...
}

try:
    new_bank_account = bank_account.create(params)
except Exception as e:
    print(e)
    raise

print(new_bank_account)
```
### Get Bank Account

```python
import pagarme_surfmappers

YOUR_API_KEY = "your_pagarme_api_key"

pagarme_surfmappers.set_api_key(YOUR_API_KEY)
bank_account = pagarme_surfmappers.BankAccount()

try:
    user_bank_account = bank_account.get()
except Exception as e:
    print(e)
    raise

print(user_bank_account)
```

## Bulk Anticipation
You can create, confirm, calcel and get limits of a bulk anticipation. Check [Pagar.me documentation](https://docs.pagar.me/v2017-08-28/reference#criando-uma-antecipa%C3%A7%C3%A3o) for more details:

```python
import pagarme_surfmappers

YOUR_API_KEY = "your_pagarme_api_key"

pagarme_surfmappers.set_api_key(YOUR_API_KEY)
bulk = pagarme_surfmappers.BulkAnticipation()
recipient_id = "some_user_recipient"
params = {
    ...
}

try:
    new_bulk = bulk.create(recipient_id, params)
except Exception as e:
    print(e)
    raise

print(new_bulk)
```
## Recipient
You can create, get and edit an recipient. You can also get an recipient balance. Check [Pagar.me documentation](https://docs.pagar.me/v2017-08-28/reference#criando-um-recebedor) for more details:

### Create Recipient
```python
import pagarme_surfmappers

YOUR_API_KEY = "your_pagarme_api_key"

params = {
    ...
}
pagarme_surfmappers.set_api_key(YOUR_API_KEY)
recipient = pagarme_surfmappers.Recipient()

try:
    new_recipient = recipient.create(params)
except Exception as e:
    print(e)
    raise

print(new_recipient)
```

### Get Recipient
```python
import pagarme_surfmappers

YOUR_API_KEY = "your_pagarme_api_key"

recipient_id = "some_user_recipient_id"
pagarme_surfmappers.set_api_key(YOUR_API_KEY)
recipient = pagarme_surfmappers.Recipient()

try:
    user_recipient = recipient.get(recipient_id)
except Exception as e:
    print(e)
    raise

print(user_recipient)
```

### Get Recipient's Balance

```python
import pagarme_surfmappers

YOUR_API_KEY = "your_pagarme_api_key"

recipient_id = 'some_user_recipient_id'
pagarme_surfmappers.set_api_key(YOUR_API_KEY)
recipient = pagarme_surfmappers.Recipient()

try:
    user_balance = recipient.get_balance(recipient_id)
except Exception as e:
    print(e)
    raise

print(user_balance)
```

## Transaction
You can create and capture an transaction. Check [Pagar.me documentation](https://docs.pagar.me/v2017-08-28/reference#criar-transacao) for more details:

### Create transaction
```python
import pagarme_surfmappers

YOUR_API_KEY = "your_pagarme_api_key"

params = {
    ...
}

pagarme_surfmappers.set_api_key(YOUR_API_KEY)
transaction = pagarme_surfmappers.Transaction()

try:
    new_transaction = transaction.create(params)
except Exception as e:
    print(e)
    raise

print(new_transaction)
```

### Capture Transcation
```python
import pagarme_surfmappers

YOUR_API_KEY = "your_pagarme_api_key"

params = {
    ...
}

pagarme_surfmappers.set_api_key(YOUR_API_KEY)
transaction = pagarme_surfmappers.Transaction()
token_id = "some_transaction_token_id"

try:
    captured_transaction = transaction.capture(token_id, params)
except Exception as e:
    print(e)
    raise

print(captured_transaction)
```

## Transfer
You can create, get and cancel an transfer. Check [Pagar.me documentation](https://docs.pagar.me/v2017-08-28/reference#criando-uma-transfer%C3%AAncia) for more details:

### Create Transfer:
```python
import pagarme_surfmappers

YOUR_API_KEY = "your_pagarme_api_key"

params = {
    ...
}

pagarme_surfmappers.set_api_key(YOUR_API_KEY)
transfer = pagarme_surfmappers.Transfer()

try:
    new_transfer = transfer.create(params)
except Exception as e:
    print(e)
    raise

print(new_transfer)
```

# Contributing and Support
Feel free to contribut to this code, improving it. Any problems can be reported in form of github issue, as any doubts. 

# License
This lib is [MIT licensed](./LICENSE).
