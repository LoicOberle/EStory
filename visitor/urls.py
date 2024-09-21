from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("list/",include("visitor.listUrls")),
    path("map/",include("visitor.mapUrls"))
   
]
