from .models import Dvd
from .filters import DvdFilter
from django_filters.constants import EMPTY_VALUES
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

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

    def get_context_data(self, **kwargs):
        ctx = super(DvdListView, self).get_context_data(**kwargs)
        ctx['filter'] = DvdFilter()
        return ctx


def search(request):
    if request.GET.get('title') in EMPTY_VALUES:
        return redirect('dvd-list')
    dvd_list = Dvd.objects.all()
    dvd_filter = DvdFilter(request.GET, queryset=dvd_list)
    return render(request, 'search/result.html', {'filter': dvd_filter})


@login_required
def rent_dvd(request, pk):
    dvd = get_object_or_404(Dvd, pk=pk)
    dvd.borrower = request.user
    dvd.save()
    return redirect(request.GET.get('next', '/'))


@login_required
def return_dvd(request, pk):
    dvd = get_object_or_404(Dvd, pk=pk)
    dvd.borrower = None
    dvd.save()
    return redirect(request.GET.get('next', '/'))


@login_required
def my_dvd(request):
    dvd_list = Dvd.objects.all().filter(borrower=request.user)
    return render(request, 'my_dvd.html', {'list': dvd_list})


