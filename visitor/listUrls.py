from django.contrib import admin
from django.urls import path,include
from . import listViews

urlpatterns = [
    path("",listViews.index_view,name="Index"),
    path("detail/<objectId>",listViews.object_detail_view,name="Object detail view"),

   
]
