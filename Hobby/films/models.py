from django.db import models
from django.contrib.auth.models import User


class Film(models.Model):
    author = models.ManyToManyField(User)
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True, upload_to='media/img/')


