from django.db import models
from django.contrib.auth.models import User
from django.db.models.constraints import CheckConstraint, UniqueConstraint
from django.utils import timezone

# Create your models here.


class Product(models.Model):
    p_name = models.CharField(max_length=100)
    p_rating = models.DecimalField(max_digits=5, decimal_places=1)
    p_description = models.CharField(max_length=500)
    p_buycount = models.IntegerField()
    p_brand = models.CharField(max_length=100)
    p_category = models.CharField(max_length=100)
    p_image = models.ImageField(upload_to="static/product_images/")
    p_price = models.DecimalField(max_digits=7, decimal_places=2)
    p_ratecount = models.IntegerField(default=0)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    class Meta:
        unique_together = ('user', 'product',)

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('user', 'product',)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_date = models.DateTimeField(default=timezone.now())
    phoneNum = models.CharField(max_length=15, default="+911234567890")
    email = models.EmailField(max_length=50, default="johndoe@email.com")
    price = models.DecimalField(max_digits=7, decimal_places=2)
    addr1 = models.CharField(max_length=200)
    fname = models.CharField(max_length=100, default="John")
    lname = models.CharField(max_length=100, default="Doe")
    rated = models.DecimalField(max_digits=7, decimal_places=2,default=-1)


class Wallet(models.Model):
    user = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=20, decimal_places=2, default=100000.00)