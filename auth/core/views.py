from django.contrib.auth import authenticate, login, logout, get_user_model
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    RetrieveUpdateAPIView,
)

from .serializers import RegistrationSerializer, UserDetailsSerializer
from rest_framework.permissions import (
    IsAuthenticated,
)
from rest_framework_simplejwt import views as jwt_views
from .utils import get_tokens_for_user
from rest_framework.response import Response
from .models import User


class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        if "email" not in request.data or "password" not in request.data:
            return Response(
                {"msg": "Credentials missing"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            auth_data = get_tokens_for_user(request.user)
            return Response(
                {"msg": "Login Success", **auth_data},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"msg": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"msg": "Successfully Logged out"}, status=status.HTTP_200_OK)


class UserDetailsView(RetrieveUpdateAPIView):
    """
    Reads and updates UserModel fields
    Accepts GET, PUT, PATCH methods.

    Read-only fields: pk, email
    Returns UserModel fields.
    """

    http_method_names = ["get", "patch"]
    serializer_class = UserDetailsSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        """
        Adding this method since it is sometimes called when using
        django-rest-swagger
        """
        return get_user_model().objects.none()
