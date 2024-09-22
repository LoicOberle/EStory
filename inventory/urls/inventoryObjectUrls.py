from django.contrib import admin
from django.urls import path,include

from ..views import inventoryObjectViews

urlpatterns = [
    #Related to pages and forms
    path("<objectId>/detail/",inventoryObjectViews.detail_view),
    path("<objectId>/infos/save",inventoryObjectViews.infos_save),
    path("<objectId>/operations/save",inventoryObjectViews.operations_save),
    path("<objectId>/loans/save",inventoryObjectViews.loans_save),
    path("<objectId>/loans/edit",inventoryObjectViews.loans_edit),

    #Rest
    path("all",inventoryObjectViews.all_objects_view,name="All objects"),
    path("create",inventoryObjectViews.new_object_view,name="New object"),
    path("<objectId>",inventoryObjectViews.object_view,name="Get an object"),
    path("<objectId>/delete",inventoryObjectViews.object_delete,name="Delete an object"),
   
]
