from django.urls import path
from . import views

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
