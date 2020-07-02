from django.db import models
from django.urls import reverse

# Create your models here.


class CreateUser(models.Model):
    name = models.CharField(max_length=256)
    age = models.IntegerField()
    email = models.CharField(max_length=256)
    gender = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:allUsers')