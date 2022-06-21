from msilib.schema import Class
from django.db import models
from django.forms import CharField


class Login(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.email 

