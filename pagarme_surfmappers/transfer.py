# -*- coding: utf-8 -*-
import pagarme_surfmappers.constants as constants
import pagarme_surfmappers.utils as utils


class Transfer(object):
    def __init__(self):
        super(Transfer, self).__init__()

    def create(self, data):
        return utils.request_post(constants.CREATE_TRANSFER_URL, data)

    def get(self, transfer_id):
        url = constants.GET_TRANSFER_URL.format(transfer_id)
        return utils.request_get(url)

    def cancel(self, transfer_id):
        url = constants.CANCEL_TRANSFER_URL.format(transfer_id)
        return utils.request_post(url)
