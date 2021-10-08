from django.urls import path
from . import views


urlpatterns = [
    path('', views.serials_index, name='serials_index'),
    path('<int:pk>/', views.serials_detail, name='serials_detail'),
    path('serial_new/', views.serials_new, name='serials_new'),
    path('my_serials/', views.my_serials, name='my_serials'),
    path('serials/<int:pk>/edit/', views.serials_edit, name='serials_edit'),
    path('delete/<int:pk>/', views.serials_delete, name='serials_delete'),
    path('add/<int:pk>/', views.serial_add, name='serial_add'),
]