from django.urls import path
from .views import *

urlpatterns=[
    path('home/',HomePage,name="home"),
    path('reg/',RegPage,name="register"),
    path('collections/',CollectionPage,name="collections")
]