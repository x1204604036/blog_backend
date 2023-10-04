
from django.http import JsonResponse


class LoginAuthMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path

        if path not in [
            "/users/register",
            "/users/login",
        ]:
            session = request.session
            if not session.get("user_id"):
                return JsonResponse({"code": -1, "msg": "not login"}, status=401)

        response = self.get_response(request)
        return response

