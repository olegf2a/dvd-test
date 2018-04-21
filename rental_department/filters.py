from .models import Dvd
import django_filters


class DvdFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', required=True)

    class Meta:
        model = Dvd
        fields = ['title', ]
