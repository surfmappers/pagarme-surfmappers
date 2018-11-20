# -*- coding: utf-8 -*-
import requests


def headers():
    _headers = {'content-type': 'application/json'}
    return _headers


def request_post(url, data, headers=headers()):
    return requests.post(url, json=data, headers=headers)
