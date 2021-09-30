from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
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


def serials_edit(request, pk):
    if request.user.is_superuser:
        tv_serial = get_object_or_404(Tvserial, pk=pk)
        if request.method == "POST":
            form = TvserialForm(request.POST, request.FILES, instance=tv_serial)
            if form.is_valid():
                serials = form.save(commit=False)
                serials.save()
                serials.author.add(User.objects.get_by_natural_key(request.user))
                return redirect('serials_detail', pk=serials.pk)
        else:
            form = TvserialForm(instance=tv_serial)
        return render(request, 'serials.html', {'form': form})
    else:
        return HttpResponse('Only admin can edit books!')


def serials_delete(request,pk):
    if request.user.is_superuser:
        serials = Tvserial.objects.all()
        context = {
            'serials': serials
        }
        try:
            book = Tvserial.objects.get(pk=pk)
            book.delete()
            return render(request, 'serials_index.html', context)
        except Tvserial.DoesNotExist:
            return HttpResponseNotFound("<h2>TVserial not found</h2>")
    else:
        return HttpResponse('Only admin can delete books!')