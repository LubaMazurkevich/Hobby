from django.contrib import admin
from .models import Book,BookSeries

admin.site.register(Book)
# Register your models here.
admin.site.register(BookSeries)

