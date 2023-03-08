import os
import requests
from django.http import HttpRequest
from rest_framework import exceptions
from rest_framework.authentication import get_authorization_header
from django.utils.encoding import smart_str


class AuthClient:
    def __init__(self, request) -> None:
        self.auth_url = os.getenv("AUTH_URL", "http://0.0.0.0:8080/api/token/verify/")
        self.request = request

    def authenticate(self) -> bool:
        token = self.get_jwt_value(self.request)
        payload_data = {"token": token}
        response = requests.post(self.auth_url, data=payload_data)
        # content = response.content
        # print(response, content)

    def get_jwt_value(self, request):
        auth = get_authorization_header(request).split()

        if not auth:
            return None

        if smart_str(auth[0].lower()) != "bearer":
            return None

        if len(auth) == 1:
            msg = _("Invalid Authorization header. No credentials provided.")
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _(
                "Invalid Authorization header. Credentials string "
                "should not contain spaces."
            )
            raise exceptions.AuthenticationFailed(msg)

        return auth[1]
