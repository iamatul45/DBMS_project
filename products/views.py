from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import Product,User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User,auth
from .forms import Register

# Create your views here.
def home(request):
    home_dict = None
    return render(request,'home.html',context=home_dict)

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',
                  {'products': products})

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
    return HttpResponse("Cart")

def profile(request):
    return HttpResponse("Profile")

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')