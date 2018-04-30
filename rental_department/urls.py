from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rental_department import views
from rental_department.api.views import UserViewSet, DvdViewSet
from django.contrib.auth.decorators import login_required

app_name = 'rental'

urlpatterns = [
    path('', views.DvdListIndexView.as_view(), name='rental'),
    path('dvd-list/', views.DvdListView.as_view(), name='dvd-list'),
    path('dvd/<int:pk>', views.DvdDetailView.as_view(), name='dvd-detail'),
    path('search', views.SearchDvdList.as_view(), name='search'),
    path('rent/<int:pk>', views.rent_dvd, name='rent-dvd'),
    path('return/<int:pk>', views.return_dvd, name='return-dvd'),
    path('my-dvd', login_required(views.MyDvdList.as_view()), name='my-dvd'),
]

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'dvd', DvdViewSet)

urlpatterns += [
    path('api/', include((router.urls, 'api'), namespace='api'))
]
