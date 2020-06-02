from django.contrib import admin
from .models import Product, Offer,User


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'description')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','password')


# Register your models here.
admin.site.register(Offer, OfferAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(User, UserAdmin)
