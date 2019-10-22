from django.db import models

class User(models.Model):
    Username=models.CharField(max_length=20)
    Email=models.EmailField(max_length=22)
    Password=models.CharField(max_length=20)

# Create your models here.
