from http.client import HTTPResponse
from django.shortcuts import render,  redirect
from .models import *
from django.contrib import messages
from .forms import *
from django.contrib.auth import authenticate,login,logout

# Create your views here.


def HomePage(request):
   return render(request,'home.html')

def logout(request):
   if request.user.is_authenticated:
      logout(request)
      messages.success(request,"logged out Successfully")
   return redirect('/')

def login(request):
   if request.user.is_authenticated:
      return redirect('home')
   else:
      if request.method =='POST':
       name=request.POST.get('username')
       pwd=request.POST.get('password')
       user=authenticate(request,username=name,password=pwd)
       if user is not None:
         login(request,user)
         messages.success(request,"logged in Successfully")
         return redirect('home/')
       else:
         messages.error(request,"invalid User Name or Password")
         return redirect('login/')
      return render(request,'login.html')
def RegPage(request):
   form=CustomUserForm()
   if request.method =='POST':
      form=CustomUserForm(request.POST)
      if form.is_valid():
         form.save()
         messages.success(request,"Registration Success You can login Now....!")
   return render(request,'reg.html',{'form':form})
def CollectionPage(request):
   catagory=Catagory.objects.filter(status=0)
   return render(request,'collections.html',{"catagory":catagory})

def Collectionviews(request,name):
   if(Catagory.objects.filter(status=0)):
      products=Product.objects.filter(category__name=name)
      return render(request,'index.html',{"products":products,"category_name":name})
   else:
      messages.warning(request,"No such Catagory Found")
      return redirect('collections')
      
def product_details(request,cname,pname):
   if(Catagory.objects.filter(name=cname,status=0)):
      if(Product.objects.filter(name=pname,status=0)):
        products = Product.objects.filter(name=pname,status=0).first()
        return render(request,"product_details.html",{"products":products})
      else:
        messages.warning(request,"No such Products Found")
        return redirect('collections')
   else:
      messages.warning(request,"No such Catagory Found")
      return redirect('collections')
      