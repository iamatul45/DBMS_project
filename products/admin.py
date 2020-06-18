from django.contrib import admin
from .models import Product, Offer,Cart,CartItem


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'description')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

class CartAdmin(admin.ModelAdmin):
    class Meta():
        model = Cart

class CartItemAdmin(admin.ModelAdmin):
    class Meta():
        model = CartItem


# Register your models here.
admin.site.register(Offer, OfferAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
