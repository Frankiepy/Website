from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Match(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

class Comment(models.Model):
    comment = models.TextField(default=" ")
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'

    #def specific for if slug = something then this

    #python manage.py makemigrations when add new thing = models.WhatEver() and
    #python manage.py migrate