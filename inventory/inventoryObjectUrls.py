from django.contrib import admin
from django.urls import path,include
from . import inventoryObjectUrls
from . import inventoryObjectViews

urlpatterns = [
    path("<objectId>/detail/",inventoryObjectViews.detail_view),
    path("<objectId>/detail/save",inventoryObjectViews.detail_save)
   
]
