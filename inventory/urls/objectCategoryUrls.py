from django.contrib import admin
from django.urls import path,include
from ..views import objectCategoryViews

urlpatterns = [

    path("all",objectCategoryViews.all_categories_view,name="All categories"),
]