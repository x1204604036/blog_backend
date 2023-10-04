import json

from django.http import JsonResponse
from django.views import View
from django.contrib.auth.hashers import check_password
from users.models import User


class UserRegisterView(View):
    """
    用户注册接口
    """
    def post(self, request):
        request_json = json.loads(request.body)
        result = User.objects.register_user(request_json)
        return JsonResponse(result, safe=False)


class UserLoginView(View):
    """
    用户登录接口
    """
    def post(self, request):
        form_data = request.POST
        username = form_data.get("username")
        password = form_data.get("password")

        if not username or not password:
            result = {"code": -1, "msg": "username or password not valid"}
        else:
            user = User.objects.filter(username=username).first()
            if not user or not check_password(password, user.password):
                result = {"code": -1, "msg": "username or password not valid"}
            else:
                request.session["user_id"] = user.id
                result = {"code": 0, "msg": "success"}
        return JsonResponse(result, safe=False)


class UserLogoutView(View):
    """
    登出接口
    """
    def post(self, request):
        if request.session.get("user_id"):
            del request.session["user_id"]
        return JsonResponse({"code": 0, "msg": "登出成功"})


class UserInfoView(View):
    """
    用户信息接口
    """
    def post(self, request):
        user_id = request.session.get("user_id")
        user_info = User.objects.get_user_info_by_id(user_id)
        return JsonResponse({"code": 0, "msg": "msg", "user_info": user_info}, safe=False)
