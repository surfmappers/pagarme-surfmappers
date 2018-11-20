import constants
import utils


class Transaction(object):
    def __init__(self, api_key):
        super(Transaction, self).__init__()
        self.api_key = api_key

    def capture(self, token, data):
        api_route = constants.CAPTURE_TRANSACTION_AFTER.format(token)
        data['api_key'] = self.api_key
        return utils.request_post(api_route, data)
