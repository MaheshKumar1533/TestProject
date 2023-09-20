from django.db import models

# Create your models here.

class userDetails(models.Model):
    name = models.CharField(max_length=30,default="name")
    #email = models.CharField(max_length=50)
    number = models.IntegerField(max_length=11)
    password = models.CharField(max_length=16,default="hars1234")