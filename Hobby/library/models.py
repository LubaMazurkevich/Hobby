from django.db import models
from django.conf import settings
# Create your models here.
from django.contrib.auth.models import User


class BookSeries(models.Model):
    title = models.CharField(max_length=100)


class Book(models.Model):
    author = models.ManyToManyField(User)
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=20)
    image = models.ImageField(null=True, blank=True, upload_to='media/img/')
    series = models.ForeignKey(BookSeries, on_delete=models.CASCADE, null=True)


