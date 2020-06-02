from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=254,null=True)
    password = models.CharField(max_length=15) 



