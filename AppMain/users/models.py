from django.db import models


class Person(models.Model):
    username = models.CharField(max_length=32, unique=True)
    email = models.EmailField(max_length=62, unique=True)
    password = models.CharField(max_length=62)
    created_at = models.DateTimeField(auto_now_add=True)
