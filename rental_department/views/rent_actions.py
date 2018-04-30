from django.contrib.auth.decorators import login_required
from rental_department.models import Dvd
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.views import generic

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


class MyDvdList(generic.ListView):
    model = Dvd
    paginate_by = 5
    template_name = 'my_dvd.html'

    def get_queryset(self):
        new_context = Dvd.objects.filter(borrower=self.request.user).order_by('id')
        return new_context



