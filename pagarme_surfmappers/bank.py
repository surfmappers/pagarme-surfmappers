# -*- coding: utf-8 -*-
import pagarme_surfmappers.constants as constants
import pagarme_surfmappers.utils as utils


class BankAccount(object):
    def __init__(self):
        super(BankAccount, self).__init__()

    def create(self, data):
        return utils.request_post(constants.CREATE_BANK_URL, data)

    def get(self, bank_account_id):
        url = constants.GET_BANK_URL.format(bank_account_id)
        return utils.request_get(url)
