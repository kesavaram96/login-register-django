from django.db import models

# Create your models here.

class user(models.Model):
    username=models.CharField(max_length=50)
    fistname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField()
    age=models.IntegerField()
    password=models.CharField(max_length=50)
    address=models.TextField()
    
    