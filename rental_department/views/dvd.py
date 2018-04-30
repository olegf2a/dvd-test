from rental_department.models import Dvd
from rental_department.filters import DvdFilter
from django.views import generic


class DvdListIndexView(generic.ListView):
    model = Dvd
    queryset = Dvd.objects.order_by('id')
    template_name = 'index.html'


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

