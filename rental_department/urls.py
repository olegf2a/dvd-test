from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rental_department import views
from rental_department.api.views import UserViewSet, DvdViewSet
app_name = 'rental'

urlpatterns = [
    path('', views.index, name='rental'),
    path('dvd-list/', views.DvdListView.as_view(), name='dvd-list'),
    path('dvd/<int:pk>', views.DvdDetailView.as_view(), name='dvd-detail'),
    path('search', views.search, name='search'),
    path('rent/<int:pk>', views.rent_dvd, name='rent-dvd'),
    path('return/<int:pk>', views.return_dvd, name='return-dvd'),
    path('my-dvd', views.my_dvd, name='my-dvd'),
]

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'dvd', DvdViewSet)

urlpatterns += [
    path('api/', include((router.urls, 'api'), namespace='api'))
]
