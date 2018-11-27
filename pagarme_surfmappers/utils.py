# -*- coding: utf-8 -*-
import requests
from pagarme_surfmappers.exceptions import RequestException

KEYS = {}


def headers():
    _headers = {'content-type': 'application/json'}
    return _headers


def check_response(response):
    status = response.status_code
    _return = response.json()
    if status == 200:
        if not _return.get('errors'):
            return _return
        else:
            raise RequestException("An error has occured", errors=_return.get('errors'))
    raise RequestException("Bad request: status code", status_code=status, errors=_return.get('errors'))


def set_api_key(api_key):
    global KEYS
    KEYS['api_key'] = api_key


def request_post(url, data, headers=headers()):
    data['api_key'] = KEYS['api_key']
    return check_response(requests.post(url, json=data, headers=headers))


def request_get(url, data={}, headers=headers()):
    data['api_key'] = KEYS['api_key']
    return check_response(requests.get(url, json=data, headers=headers))


def request_put(url, data, headers=headers()):
    data['api_key'] = KEYS['api_key']
    return check_response(requests.put(url, json=data, headers=headers))
