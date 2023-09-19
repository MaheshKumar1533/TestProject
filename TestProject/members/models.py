from django.db import models

# Create your models here.

class userDetails(models.Model):
    number = models.BigIntegerField(max_length=11)
    password = models.CharField(max_length=16)