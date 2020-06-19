from django.urls import path
from . import views


urlpatterns = [
    path('',views.home),
    path('products/', views.index),
    path('login/',views.login),
    path('register/',views.register),
    path('cart/',views.cart),
    path('about/',views.about),
    path('profile/',views.profile),
    path('logout/',views.logout),
    path('add/<int:id>',views.add),
    path('cart/checkout/',views.checkout),
    path('cart/remove/<int:id>',views.remove),
    path('cart/quantity/<int:id>',views.quantity),
    path('cart/checkout/thankyou/',views.thankyou)
]