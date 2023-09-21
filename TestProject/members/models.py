from django.db import models

# Create your models here.

class userDetails(models.Model):
    name = models.CharField(max_length=30,default="name")
    #email = models.CharField(max_length=50)
    number = models.IntegerField(max_length=11)
    password = models.CharField(max_length=16,default="hars1234")

class merchant_details(models.Model):
    phone_number = models.IntegerField(max_length=10)
    name = models.CharField(max_length=30)
    shop_name = models.CharField(max_length=30)
    address = models.CharField(max_length=70)
    pincode = models.IntegerField(max_length=6)

class customer_details(models.Model):
    phone_number = models.IntegerField(max_length=10)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=70)
    pincode = models.IntegerField(max_length=6)

class merchant_stock(models.Model):
    merchant_id = models.ForeignKey(merchant_details, models.CASCADE)
    product_id = models.ForeignKey(products, models.CASCADE)
    stock_available = models.IntegerField(max_length=5)

class product_details(models.Model):
    product_name = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)

class orders(models.Model):
    merchant_id = models.ForeignKey(merchant_details, models.CASCADE)
    customer_id = models.ForeignKey(customer_details, models.CASCADE)
    product_id = models.ForeignKey(products, models.CASCADE)
    payment_status = models.CharField(max_length=10)
    order_location = models.ForeignKey(customer_details, modles.CASCADE)