from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import Product,User
from django.contrib.auth import authenticate
from .forms import Register

# Create your views here.
def home(request):
    home_dict = None
    return render(request,'home.html',context=home_dict)

def index(request):
    # return HttpResponse('Hello World')
    products = Product.objects.all()
    return render(request, 'index.html',
                  {'products': products})

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username,password = password)
        if user is not None:
            return HttpResponseRedirect('/')
        
    else:
        return render(request,'login.html')

  
def register(request):
    if request.method == 'POST': 
        user = Register(request.POST)
        user.save()
        return HttpResponseRedirect('/') 
    else:
        context ={} 
        context['form']= Register()
        return render(request, "register.html", context) 