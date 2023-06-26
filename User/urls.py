from django.urls import path
from .views import UserApiView, UserRegister, UserLoginApi, UserLogout, UserPasswordUpdateApi, UserUpdateApi

urlpatterns = [
    path('', UserApiView.as_view(), name='user_view'),
    path('register/', UserRegister.as_view(), name='user_register'),
    path('login/', UserLoginApi.as_view(), name='user_login'),
    path('logout/', UserLogout.as_view(), name='user_logout'),
    path('update/', UserUpdateApi.as_view(), name='user-update'),
    path('update/password', UserPasswordUpdateApi.as_view(), name='user_password-update'),

]
