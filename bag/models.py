from django.db import models

# Create your models here.
class Guser(models.Model):
    username = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100) 
class items(models.Model):
    username = models.ForeignKey(Guser, on_delete = models.CASCADE)
    name = models.CharField(max_length=100, primary_key=True)
    quantity = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    date = models.DateField()