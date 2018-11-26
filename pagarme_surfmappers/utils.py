# -*- coding: utf-8 -*-
import requests
from pagarme_surfmappers.exceptions import RequestException

KEYS = {}


def headers():
    _headers = {'content-type': 'application/json'}
    return _headers


def check_response(response):
    if response.status == 200:
        if not response.get("errors"):
            return response
        else:
            raise RequestException("Something whent wrong: " + response.get('errors'))
            return
    raise RequestException("Bad request: status code" + str(response.status))


def set_api_key(api_key):
    global KEYS
    KEYS['api_key'] = api_key


def request_post(url, data, headers=headers()):
    data['api_key'] = KEYS['api_key']
    return check_response(requests.post(url, json=data, headers=headers))


def request_get(url, data={}, headers=headers()):
    data['api_key'] = KEYS['api_key']
    return check_response(requests.get(url))


def request_put(url, data, headers=headers()):
    data['api_key'] = KEYS['api_key']
    return check_response(requests.put(url, json=data, headers=headers))
