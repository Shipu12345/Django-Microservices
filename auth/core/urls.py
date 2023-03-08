from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import (
    RegistrationView,
    LoginView,
    LogoutView,
    UserDetailsView,
)


app_name = "users"

urlpatterns = [
    path("accounts/register", RegistrationView.as_view(), name="register"),
    path("accounts/login", LoginView.as_view(), name="login"),
    path("accounts/logout", LogoutView.as_view(), name="logout"),
    path(
        "accounts/token-refresh/",
        jwt_views.TokenRefreshView.as_view(),
        name="token_refresh",
    ),

    path("token/verify/", jwt_views.TokenVerifyView.as_view(), name="token_verify"),
    path("user/", UserDetailsView.as_view(), name="rest_user_details"),
]
