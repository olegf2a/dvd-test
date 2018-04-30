# Serializers define the API representation.
from rest_framework import serializers
from django.contrib.auth.models import User
from rental_department.models import Dvd


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class DvdSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dvd
        fields = ('title', 'summary', 'borrower')
