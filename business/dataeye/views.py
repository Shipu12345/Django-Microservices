from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import exceptions, status
from rest_framework.viewsets import GenericViewSet

from .serializers import StoreSerializer
from rest_framework.mixins import (
    RetrieveModelMixin,
    ListModelMixin,
)
import json
from .models import Store
from business.auth_client.auth import AuthClient
from .helpers import RequestDataDistance

class StoreViewSet(RetrieveModelMixin, GenericViewSet, ListModelMixin):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    def get_queryset(self):
        is_verified = AuthClient(self.request).authenticate()
        if not is_verified:
            msg = "Invalid Authorization header. No credentials provided."
            raise exceptions.AuthenticationFailed(msg)
    
        get_data = self.request.GET
        if 'lat' not in  get_data:
            msg = "No Lat Provided"
            raise exceptions.APIException(msg)
        lat  = get_data['lat']

        if 'long' not in  get_data:
            msg = "No Long Provided"
            raise exceptions.APIException(msg)
        long = get_data['long']
        distance_obj = RequestDataDistance(lat, long)

        print(distance_obj)

        # return super().get_queryset()
        return Store.objects.filter()
