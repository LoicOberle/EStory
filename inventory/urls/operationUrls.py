from django.contrib import admin
from django.urls import path,include
from views import operationViews

urlpatterns = [

    path("<objectId>/all",operationViews.all_operations_view,name="All operations"),
]