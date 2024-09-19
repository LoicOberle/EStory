from django.contrib import admin
from django.urls import path,include
from . import inventoryObjectUrls
from . import inventoryObjectViews

urlpatterns = [
    path("<objectId>/detail/",inventoryObjectViews.detail_view),
    path("<objectId>/infos/save",inventoryObjectViews.infos_save),
    path("<objectId>/operations/save",inventoryObjectViews.operations_save),
    path("<objectId>/loans/save",inventoryObjectViews.loans_save),
    path("<objectId>/loans/edit",inventoryObjectViews.loans_edit),
   
]
