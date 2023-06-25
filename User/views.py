from django.contrib.auth import login, logout
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from User.models import User
from .serializer import Userserializer, RegisterSerializer, LoginSerializer, LogoutSerializer


# Create your views here.

class UserApiView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = User.objects.filter(id=request.user.id)
        serializer_class = Userserializer(queryset, many=True)
        return Response(serializer_class.data, status=status.HTTP_200_OK)


class UserRegister(generics.CreateAPIView):
    queryset = User.objects.all()

    def get_serializer_class(self):
        return RegisterSerializer




class UserLoginApi(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        user = User.objects.filter(username=username, password=password).first()
        if user:
            login(request, user=user)
            return Response(serializer.data)
        else:
            return Response({"detail": "error"})


class UserLogout(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ask = serializer.validated_data.get('ask_logout')
        user = request.user
        if ask in ['Yes', 'yes']:
            logout(request)
            return Response({"detail": f"Logout from {user}"})
        else:
            return Response(status=status.HTTP_200_OK)

# a = {
#     "username": "salom",
#     "old_password": "salom77A",
#     "new_password": "salom88A",
#
# }
