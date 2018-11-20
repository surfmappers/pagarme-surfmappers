# -*- coding: utf-8 -*-
import constants
import utils


class Transaction(object):
    def __init__(self):
        super(Transaction, self).__init__()

    def create(self, data):
        return utils.request_post(constants.CREATE_TRANSACTION_URL, data)

    def capture(self, token, data):
        api_route = constants.CAPTURE_TRANSACTION_URL.format(token)
        return utils.request_post(api_route, data)
