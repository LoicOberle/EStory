from django.contrib import admin
from django.urls import path,include
from . import inventoryViews

urlpatterns = [
    
    path("object/<objectId>/changes/<field>",inventoryViews.all_changes_view,name="All loans"),

]
