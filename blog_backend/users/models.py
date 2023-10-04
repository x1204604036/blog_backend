from django.db import models
from django.contrib.auth.hashers import make_password
from utils.common_exception import CommonException


class BaseModel(models.Model):
    updated_time = models.DateTimeField(auto_now=True)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class UserManager(models.Manager):
    def register_user(self, user_info):
        username = user_info.get("username")
        password = user_info.get("password")
        email = user_info.get("email")

        if not username or not password or not email:
            result = {"code": -1, "msg": "username or password not valid"}
        else:
            if self.filter(username=username).exists():
                result = {"code": -1, "msg": "username exists"}
            else:
                User.objects.create(username=username, password=make_password(password), email=email)
                result = {"code": 0, "msg": "success"}
        return result

    def get_user_info_by_id(self, user_id):
        user = self.filter(id=user_id).first()

        if not user:
            raise CommonException(status_code=-1, error_msg="user_id 不正确", http_code=200)
        return user.info()


class User(BaseModel):
    username = models.CharField(verbose_name="用户名", max_length=50, unique=True)
    password = models.CharField(verbose_name="密码", max_length=200)
    email = models.CharField(verbose_name="邮箱", max_length=50, unique=True)

    objects = UserManager()

    def info(self):
        return {
            "user_id": self.id,
            "username": self.username,
            "email": self.email,
        }
