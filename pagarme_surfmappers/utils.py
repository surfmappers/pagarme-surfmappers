# -*- coding: utf-8 -*-
import requests

KEYS = {}


def headers():
    _headers = {'content-type': 'application/json'}
    return _headers


def set_api_key(api_key):
    global KEYS
    KEYS['api_key'] = api_key


def request_post(url, data, headers=headers()):
    data['api_key'] = KEYS['api_key']
    return requests.post(url, json=data, headers=headers)


def request_get(url, data={}, headers=headers()):
    data['api_key'] = KEYS['api_key']
    return requests.get(url)
