from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .forms import TvserialForm
from .models import Tvserial
from django.shortcuts import redirect
from django.contrib.auth.models import User


def serials_index(request):
    serials=Tvserial.objects.all()
    context = {
        'serials': serials
    }
    return render(request, 'serials_index.html', context)


def serials_detail(request,pk):
    tv_serial=Tvserial.objects.get(pk=pk)
    context={
        'tv_serial': tv_serial
    }
    return render(request, 'serials_detail.html', context)


def serials_new(request):
    if request.method == "POST":
        form = TvserialForm(request.POST, request.FILES)
        if form.is_valid():
            serials = form.save(commit=False)
            serials.save()
            serials.author.add(User.objects.get_by_natural_key(request.user))
            return redirect('serials_detail', pk=serials.pk)
    else:
        form = TvserialForm()
    return render(request, 'serials.html', {'form': form})


def my_serials(request):
    if request.user.is_authenticated:
        my_serials = Tvserial.objects.filter(author=request.user)
        context = {
            'my_serials': my_serials
        }

        return render(request, 'my_serials.html', context)
    else:
        return HttpResponse('No authenticated,please login and then add books')
