from django.urls import path
from .views import *

urlpatterns=[
    path('',HomePage,name="home"),
    path('reg/',RegPage,name="register"),
    path('login/',login,name="login"),
    path('logout/',logout,name="logout"),
    path('collections/',CollectionPage,name="collections"),
    path('coloutctions/',CollectionPage,name="collections"),
    path('collections/<str:name>/',Collectionviews,name="collections"),
    path('collections/<str:cname>/<str:pname>',product_details,name="product_details")
]