# -*- coding: utf-8 -*-
import pagarme_surfmappers.constants as constants
import pagarme_surfmappers.utils as utils


class Recipient(object):
    def __init__(self):
        super(Recipient, self).__init__()

    def create(self, data):
        return utils.request_post(constants.CREATE_RECIPIENT_URL, data)

    def get(self, recipient_id):
        url = constants.GET_RECIPIENT_URL.format(recipient_id)
        return utils.request_get(url)

    def edit(self, recipient_id, data):
        url = constants.GET_RECIPIENT_URL.format(recipient_id)
        return utils.request_put(url, data)

    def get_balance(self, recipient_id):
        url = constants.GET_RECIPIENT_BALANCE_URL.format(recipient_id)
        return utils.request_get(url)
