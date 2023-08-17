
class CommonException(Exception):
    def __init__(self, status_code=-1, error_msg="error inf", http_code=500):
        self.status_code = status_code
        self.error_msg = error_msg
        self.http_code = http_code
