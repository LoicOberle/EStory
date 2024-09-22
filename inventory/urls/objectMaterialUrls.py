from django.contrib import admin
from django.urls import path,include
from ..views import objectMaterialViews

urlpatterns = [
     path("all",objectMaterialViews.all_materials_view,name="All materials"),
]