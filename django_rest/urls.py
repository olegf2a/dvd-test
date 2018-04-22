from django.urls import path

from django_rest.api.views import UserViewSet, DvdViewSet
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'dvd', DvdViewSet)

urlpatterns = [
    path('', include('rest_framework.urls')),
    path('', include(router.urls))
]
