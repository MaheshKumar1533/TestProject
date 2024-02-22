from django.db import models
from django.contrib.auth.models import AbstractUser

class userDetails(AbstractUser):
    username = models.CharField(max_length=30,default="Harsha123",primary_key=True)
    last_login = models.DateTimeField(null=True, blank=True)
    REQUIRED_FIELDS = ['email']

class merchant_details(models.Model):
    merchant_id = models.IntegerField()
    name = models.CharField(max_length=30)
    shop_name = models.CharField(max_length=30)
    address = models.CharField(max_length=70)
    pincode = models.IntegerField()

class customer_details(models.Model):
    phone_number = models.IntegerField()
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=70)
    pincode = models.IntegerField()

class product_details(models.Model):
    product_id = models.IntegerField() 
    product_name = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)

class merchant_stock(models.Model):
    merchant_id = models.ForeignKey(merchant_details, on_delete=models.CASCADE)
    product_id = models.ForeignKey(product_details, on_delete=models.CASCADE)
    stock_available = models.IntegerField()

class orders(models.Model):
    merchant_id = models.ForeignKey(merchant_details, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(customer_details, on_delete=models.CASCADE)
    product_id = models.ForeignKey(product_details, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=10)
    order_location = models.ForeignKey(customer_details, on_delete=models.CASCADE, related_name="order_locations")