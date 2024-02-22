from django.db import models
from django.contrib.auth.models import User

class OTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    otp_code = models.CharField(max_length=6)
    creation_time = models.DateTimeField(auto_now_add=True)

