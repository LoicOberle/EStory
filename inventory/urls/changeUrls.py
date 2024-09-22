from django.contrib import admin
from django.urls import path,include
from views import changeViews

urlpatterns = [

   path("<objectId>/<field>/all",changeViews.all_changes_view,name="All changes"),
]