from django.contrib import admin
from django.urls import path,include
from ..views import groupViews

urlpatterns = [
      path("groups",groupViews.all_groups_view,name="All groups"),
]