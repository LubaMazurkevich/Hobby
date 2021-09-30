from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .forms import FilmForm

# Create your views here.
from .models import Film
from django.shortcuts import redirect
from django.contrib.auth.models import User


def film_index(request):
    films=Film.objects.all()
    context = {
        'films': films
    }
    return render(request, 'film_index.html', context)


def film_detail(request,pk):
    film=Film.objects.get(pk=pk)
    context={
        'film': film
    }
    return render(request, 'film_detail.html', context)


def film_new(request):
    if request.method == "POST":
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            film = form.save(commit=False)
            film.save()
            film.author.add(User.objects.get_by_natural_key(request.user))
            return redirect('film_detail', pk=film.pk)
    else:
        form = FilmForm()
    return render(request, 'films.html', {'form': form})


def my_films(request):
    if request.user.is_authenticated:
        my_films = Film.objects.filter(author=request.user)
        context = {
            'my_films': my_films
        }

        return render(request, 'my_films.html', context)
    else:
        return HttpResponse('No authenticated,please login and then add books')


def film_edit(request, pk):
    if request.user.is_superuser:
        film = get_object_or_404(Film, pk=pk)
        if request.method == "POST":
            form = FilmForm(request.POST, request.FILES, instance=film)
            if form.is_valid():
                film = form.save(commit=False)
                film.save()
                film.author.add(User.objects.get_by_natural_key(request.user))
                return redirect('film_detail', pk=film.pk)
        else:
            form = FilmForm(instance=film)
        return render(request, 'films.html',{'form':form})
    else:
        return HttpResponse('Only admin can edit books!')


def film_delete(request, pk):
    if request.user.is_superuser:
        films = Film.objects.all()
        context = {
            'films': films
        }
        try:
            film = Film.objects.get(pk=pk)
            film.delete()
            return render(request, 'film_index.html', context)
        except Film.DoesNotExist:
            return HttpResponseNotFound("<h2>Film not found</h2>")
    else:
        return HttpResponse('Only admin can delete books!')
