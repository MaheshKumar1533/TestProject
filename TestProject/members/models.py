from django.db import models

# Create your models here.

class userDetails(models.Model):
    number = models.IntegerField(max_length=11)
    password = models.CharField(max_length=16)