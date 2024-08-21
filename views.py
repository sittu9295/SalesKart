from django.shortcuts import render, redirect
from .forms import *
# Create your views here.


def HomePage(request):
   context={

   }
   return render(request,'home.html',context)
def RegPage(request):
   context={

   }
   return render(request,'reg.html',context)
def CollectionPage(request):
   catagory=Catagory.objects.filter(status=0)
   return render(request,'collections.html',{"catagory":catagory})