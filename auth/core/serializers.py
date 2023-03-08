from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.conf import settings
from .models import User

UserModel = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["user_name", "email", "password"]
        extra_kwargs = {"password": {"write_only": True, "required": True}}

    def save(self):
        user = User(email=self.validated_data["email"])
        password = self.validated_data["password"]
        user.user_name = self.validated_data["user_name"]

        user.set_password(password)
        user.save()
        return user


class UserDetailsSerializer(serializers.ModelSerializer):
    @staticmethod
    def validate_username(username):
        return username

    class Meta:
        extra_fields = []

        if hasattr(UserModel, "USERNAME_FIELD"):
            extra_fields.append(UserModel.USERNAME_FIELD)
        if hasattr(UserModel, "EMAIL_FIELD"):
            extra_fields.append(UserModel.EMAIL_FIELD)
        if hasattr(UserModel, "user_name"):
            extra_fields.append("user_name")
        if hasattr(UserModel, "first_name"):
            extra_fields.append("first_name")
        if hasattr(UserModel, "first_name"):
            extra_fields.append("first_name")
        if hasattr(UserModel, "last_name"):
            extra_fields.append("last_name")
        
        model = UserModel
        fields = ("pk", *extra_fields)
        read_only_fields = ("email",)
