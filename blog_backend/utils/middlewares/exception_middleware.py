import traceback
from django.http import JsonResponse
import logging

logger = logging.getLogger("error_logger")


class ExceptionMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        code = -1
        error_msg = "error"
        status = 500

        if hasattr(exception, "error_msg"):
            error_msg = getattr(exception, "error_msg", "")
            code = getattr(exception, "status_code", -1)
            status = getattr(exception, "http_code", 500)
            traceback_info = error_msg
        else:
            traceback_info = traceback.format_exc()
        logger.warning(f"request_path: {request.path}, traceback_info: {traceback_info}")
        return JsonResponse({"code": code, "msg": error_msg}, status=status)

