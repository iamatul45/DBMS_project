from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

    def __str__(self):
        return self.name


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True,on_delete=callable)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, null=True, blank=True,on_delete=callable)
    product = models.ForeignKey(Product,on_delete=callable)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)



