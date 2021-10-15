from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from .forms import FilmForm
from .models import Film
from django.shortcuts import redirect
from django.contrib.auth.models import User
import requests
from bs4 import BeautifulSoup
import json
from django.conf import settings
import os

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


def create_film_link(request):
    return render(request, 'form_by_link.html')


def create_film_link_(request):
    url = request.GET['link']
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('script', type="application/ld+json")
    string = str(quotes)
    start = string.find('{')
    end = string.rfind("}")
    dct = string[start:end+1]
    d = json.loads(dct)
    film = Film()

    image=d['publisher']['logo']['url']
    filename=image.split('/')[-1]
    film.image = os.path.join("img", filename)
    filename = os.path.join(settings.MEDIA_ROOT, "img", filename)
    r=requests.get(image, allow_redirects=True)
    open(filename, "wb").write(r.content)

    film.title = d['name']
    film.description = d['description']

    genres = soup.find_all('span', itemprop="genre")
    genre_result=""
    for genre in genres:
        genre_result = genre.text[:50]
    film.genre = genre_result
    film.save()






    return render(request, 'my_films.html')

