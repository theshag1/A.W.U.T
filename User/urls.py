from django.urls import path
from .views import UserApiView, UserRegister, UserLoginApi, UserLogout

urlpatterns = [
    path('', UserApiView.as_view(), name='user_view'),
    path('register/', UserRegister.as_view(), name='user_register'),
    path('login/', UserLoginApi.as_view(), name='user_login'),
    path('logout/', UserLogout.as_view(), name='user_logout'),

]
