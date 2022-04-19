import django
from django.shortcuts import render,HttpResponse
from requests import request
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib import messages
from django.db.models import Q


def home(request):
    prod = Product.objects.all()
    return render(request,'home.html',{'prod':prod})

def search(request):
    query = request.GET['query']
    multiple_q = Q(Q(product_name__icontains=query) | Q(Q(price__icontains=query)) )
    searchproduct = Product.objects.filter(multiple_q)  
    return render(request,'search.html', {'searchproduct':searchproduct})

    


def user_signup(request):
        return render(request,'signup.html')

def login(request):
    return render(request,'login.html')




      
         





    

