from django.urls import path
from . import views


urlpatterns = [
    path('', views.film_index, name='film_index'),
    path('<int:pk>/', views.film_detail, name='film_detail'),
    path('film_new/', views.film_new, name='film_new'),
    path('my_films/', views.my_films, name='my_films'),
    path('film/<int:pk>/edit/', views.film_edit, name='film_edit'),
    path('delete/<int:pk>/', views.film_delete, name='film_delete'),
    path('film_new_by_link/', views.create_film_link , name='film_new_by_link'),
    path('create_film_link_/', views.create_film_link_,name='create_film_link_'),

]