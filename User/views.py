from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from User.models import User
from .serializer import Userserializer, RegisterSerializer, LoginSerializer, LogoutSerializer, UserUpdateSerializer, \
    UserUpdatePasswordSerializer


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
        user = User.objects.filter(username=username).first()
        is_valid = check_password(password, user.password)
        if is_valid:
            login(request, user=user)
            return Response(serializer.data)
        else:
            return Response({"Error": "Correct user or password"})


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


class UserPasswordUpdateApi(APIView):
    def get(self, request, *args, **kwargs):
        queryset = User.objects.filter(id=request.user.id)
        serializer_class = Userserializer(queryset, many=True)
        return Response(serializer_class.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = UserUpdatePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username')
        user = User.objects.filter(username=username).first()
        password = serializer.validated_data.get('password')
        new_password = serializer.validated_data.get('new_password')
        is_validate = check_password(password, user.password)
        if is_validate:
            user.set_password(new_password)
            user.save()
            return Response(serializer.data)
        else:
            return Response({"error": "Correct username or password"})


class UserUpdateApi(APIView):
    def get(self, request, *args, **kwargs):
        queryset = User.objects.filter(id=request.user.id)
        serializer = UserUpdateSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        user = User.objects.filter(id=request.user.id)
        serializer = UserUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username')
        user.update(username=username)
        return Response(serializer.data)
