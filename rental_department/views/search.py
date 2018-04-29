from rental_department.models import Dvd
from rental_department.filters import DvdFilter
from django_filters.constants import EMPTY_VALUES
from django.shortcuts import render, redirect


def search(request):
    if request.GET.get('title') in EMPTY_VALUES:
        return redirect('dvd-list')
    dvd_list = Dvd.objects.all()
    dvd_filter = DvdFilter(request.GET, queryset=dvd_list)
    return render(request, 'search/result.html', {'filter': dvd_filter})