from rental_department.models import Dvd
from rental_department.filters import DvdFilter
from django.views import generic


class SearchDvdList(generic.ListView):
    model = Dvd
    paginate_by = 5
    template_name = 'search/result.html'

    def get_queryset(self):
        # TODO fix bug with missing query during pagination
        return Dvd.objects.filter(title__contains=self.request.GET.get('title')).order_by('id')

    def get_context_data(self, **kwargs):
        ctx = super(SearchDvdList, self).get_context_data(**kwargs)
        ctx['filter'] = DvdFilter(self.request.GET)
        return ctx
