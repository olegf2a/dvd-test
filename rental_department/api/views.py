# Create your views here.
from rental_department.api.serializers import UserSerializer, DvdSerializer
from django.contrib.auth.models import User
from rental_department.models import Dvd
from rest_framework import viewsets
from django.views import generic

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DvdViewSet(viewsets.ModelViewSet):
    queryset = Dvd.objects.all()
    serializer_class = DvdSerializer


class UserDetailView(generic.DetailView):
    model = User
    serializer_class = UserSerializer
