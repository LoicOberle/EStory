from django.contrib import admin
from django.urls import path,include
from views import roomViews

urlpatterns = [

    path("all",roomViews.all_rooms_view,name="All rooms"),
]