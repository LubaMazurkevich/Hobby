from django.urls import path
from . import views
# from .views import SearchResultsView

urlpatterns = [
    path('search/', views.search_results, name='search_results')]