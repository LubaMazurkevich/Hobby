from django.urls import path
from . import views


urlpatterns = [
    path('', views.film_index, name='film_index'),
    path('<int:pk>/', views.film_detail, name='film_detail'),
    path('film_new/', views.film_new, name='film_new'),
    path('my_films/', views.my_films, name='my_films'),
]