# myapp/models.py
from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=100)

class Publisher(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author, related_name='books', related_query_name='book')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='books', related_query_name='book')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', related_query_name='profile')
    bio = models.TextField()
