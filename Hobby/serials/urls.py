from django.urls import path
from . import views


urlpatterns = [
    path('', views.serials_index, name='serials_index'),
    path('<int:pk>/', views.serials_detail, name='serials_detail'),
    path('film_new/', views.serials_new, name='serials_new'),
    path('my_films/', views.my_serials, name='my_serials'),
]