from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _

from User.models import User


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'user_phone',
            'first_name',
            'last_name',
            'user_ball',

        )
        read_only_fields = ('id',)


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'user_phone',
            'password'
        )
        read_only_fields = ('id',)

    def validate(self, attrs):
        password = attrs.get('password')
        if not password:
            raise ValidationError(_("Password didn't match"))
        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop('password', )
        user = User(**validated_data)
        user.set_password(make_password(password=password))
        user.save()
        return user



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class LogoutSerializer(serializers.Serializer):
    ask_logout = serializers.CharField(max_length=3)
