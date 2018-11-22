# -*- coding: utf-8 -*-
import constants
import utils


class BankAccount(object):
    def __init__(self):
        super(BankAccount, self).__init__()

    def create(self, data):
        utils.request_post(constants.CREATE_BANK_URL, data)
