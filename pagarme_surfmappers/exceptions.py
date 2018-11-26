class RequestException(Exception):
    def __init__(self, message, status_code=200, errors={}):
        message += ' - Status code:' + str(status_code)
        if errors:
            message += ' - erros: ' + str(errors)
        super(RequestException, self).__init__(message)
