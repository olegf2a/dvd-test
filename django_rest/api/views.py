from django.shortcuts import render

# Create your views here.
from django_rest.api.serializers import UserSerializer, DvdSerializer
from django.contrib.auth.models import User
from rental_department.models import Dvd
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DvdViewSet(viewsets.ModelViewSet):
    queryset = Dvd.objects.all()
    serializer_class = DvdSerializer
