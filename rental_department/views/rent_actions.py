from django.contrib.auth.decorators import login_required
from rental_department.models import Dvd
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect


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


