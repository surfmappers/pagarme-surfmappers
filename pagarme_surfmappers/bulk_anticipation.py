# -*- coding: utf-8 -*-
import pagarme_surfmappers.constants as constants
import pagarme_surfmappers.utils as utils


class BulkAnticipation(object):
    def __init__(self):
        super(BulkAnticipation, self).__init__()

    def create(self, recipient_id, data):
        url = constants.CREATE_BULK_ANTICIPATION_URL.format(recipient_id)
        return utils.request_post(url, data)

    def limits(self, recipient_id, data):
        url = constants.GET_BULK_LIMITS.format(recipient_id)
        return utils.request_get(url, data=data)

    def confirm(self, recipient_id, bulk_id):
        url = constants.CONFIRM_BULK_ANTICIPATION.format(recipient_id, bulk_id)
        return utils.request_post(url, data={})

    def cancel(self, recipient_id, bulk_id):
        url = constants.CANCEL_BULK_ANTICIPATION.format(recipient_id, bulk_id)
        return utils.request_post(url, data={})
