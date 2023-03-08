from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import StoreSerializer
from rest_framework.mixins import (
    RetrieveModelMixin,
    ListModelMixin,
)
from rest_framework.viewsets import GenericViewSet
from .models import Store
from  business.auth_client.auth import AuthClient


class StoreViewSet(RetrieveModelMixin, GenericViewSet, ListModelMixin):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    
    def get_queryset(self):
        print(self, AuthClient(self.request).authenticate())
        return super().get_queryset()