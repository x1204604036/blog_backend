from django.urls import path
from users.views import UserRegisterView, UserLoginView, UserLogoutView, UserInfoView

urlpatterns = [
    path("register", UserRegisterView.as_view()),
    path("login", UserLoginView.as_view()),
    path("logout", UserLogoutView.as_view()),
    path("user_info", UserInfoView.as_view()),
]
