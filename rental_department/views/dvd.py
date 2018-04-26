from rental_department.models import Dvd
from rental_department.filters import DvdFilter
from django.views import generic
from django.shortcuts import render


def index(request):
    num_dvd = Dvd.objects.all().count()
    return render(
        request,
        'index.html',
        context={'num_dvd': num_dvd, },
    )


class DvdDetailView(generic.DetailView):
    model = Dvd


class DvdListView(generic.ListView):
    model = Dvd
    paginate_by = 5
    queryset = Dvd.objects.order_by('id')

    def get_context_data(self, **kwargs):
        ctx = super(DvdListView, self).get_context_data(**kwargs)
        ctx['filter'] = DvdFilter()
        return ctx

