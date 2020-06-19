from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect,reverse,resolve_url
from .models import Product,User,CartItem,Cart
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from decimal import Decimal

# Create your views here.
def home(request):
    total_count = get_cart_count(request)
    return render(request,'home.html',{'total_count':total_count})
    
@login_required(login_url='/products/login/')
def index(request):
    products = Product.objects.all()
    total_count = get_cart_count(request)
    cart = get_user_cart(request)
    items = CartItem.objects.filter(cart=cart)
    app=[]
    for i in items:
        app.append(i.product.id)
    return render(request, 'index.html',
                  {'products': products,'total_count':total_count,'app':app})

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username,password = password)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect("/")
        else:
            messages.error(request,'Invalid credentials.')
            return HttpResponseRedirect('/login')
        
    else:
        return render(request,'login.html')

  
def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.error(request,"Username Not Available.")
                return HttpResponseRedirect('/register')
            elif User.objects.filter(email = email).exists():
                messages.error(request,"Email already registered.")
                return HttpResponseRedirect('/register')
            else:
                user = User.objects.create_user(first_name = first_name,last_name = last_name,username = username,email = email,password = password1)
                user.save()
                return HttpResponseRedirect('/login')
        else:
            messages.error(request,"Password do not Match.")
            return HttpResponseRedirect('/register')
    else:
        return render(request,'register.html') 

def cart(request):
    return view_cart(request)

def about(request):
    return render(request,'about.html')

def profile(request):
    total_count = get_cart_count(request)
    return render(request,'profile.html',{'total_count':total_count})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/products/login/')
def add(request,id):
    cart = get_user_cart(request)
    product = Product.objects.get(id=id)
    quantity = 1
    cart_item = CartItem(product=product, cart=cart, quantity=0)
    cart_item.quantity += quantity
    cart_item.save()
    if request.session.get('cart_count'):
        request.session['cart_count'] += quantity
    else:
        request.session['cart_count'] = quantity
    update_cart_info(request)
    return HttpResponseRedirect('/products')

def view_cart(request):
    cart = get_user_cart(request)
    cart_items = CartItem.objects.filter(cart=cart)
    order_total = 0
    total_count=0
    for item in cart_items:
        total_count += item.quantity
    for item in cart_items:
        order_total += (item.product.price * item.quantity)
    return render(request,'cart.html',{'cart_items':cart_items,'total_count':total_count,'order_total':order_total})

def update_cart_info(request):
    request.session['cart_count'] = get_cart_count(request)

def get_cart_count(request):
    cart = get_user_cart(request)
    total_count = 0
    cart_items = CartItem.objects.filter(cart=cart)
    for item in cart_items:
        total_count += item.quantity
    return (total_count)


def get_user_cart(request):
    """Retrieves the shopping cart for the current user."""
    cart_id = None
    cart = None
    # If the user is logged in, then grab the user's cart info.
    if request.user.is_authenticated and not request.user.is_anonymous:
        try:
            cart = Cart.objects.get(user=request.user)
        except Cart.DoesNotExist:
            cart = Cart(user=request.user)
            cart.save()
    else:
        cart_id = request.session.get('cart_id')
        if not cart_id:
            cart = Cart()
            cart.save()
            request.session['cart_id'] = cart.id
        else:
            cart = Cart.objects.get(id=cart_id)
    return cart

def remove(request,id):
    product = Product.objects.get(id=id)
    cart_item = CartItem.objects.get(product=product)
    cart_item.delete()
    update_cart_info(request)
    return HttpResponseRedirect('/cart')


def checkout(request):
    cart = get_user_cart(request)
    cart_items = CartItem.objects.filter(cart=cart)
    order_total=0
    for item in cart_items:
        order_total += (item.product.price * item.quantity)
    return render(request,'checkout.html',{'order_total':order_total})


def thankyou(request):
    return render(request,'thankyou.html')

def quantity(request,id):
    product = Product.objects.get(id=id)
    cart_item = CartItem.objects.get(product=product)
    cart_item.quantity+=1
    cart_item.save()
    update_cart_info(request)
    return HttpResponseRedirect('/cart')
