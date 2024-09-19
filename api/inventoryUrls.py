from django.contrib import admin
from django.urls import path,include
from . import inventoryViews

urlpatterns = [
    path("objects",inventoryViews.all_objects_view,name="All objects"),
    path("objects/create",inventoryViews.new_object_view,name="New object"),
    path("object/<objectId>",inventoryViews.object_view,name="Get an object"),
    path("object/<objectId>/delete",inventoryViews.object_delete,name="Delete an object"),
    path("categories",inventoryViews.all_categories_view,name="All categories"),
    path("materials",inventoryViews.all_materials_view,name="All materials"),
    path("rooms",inventoryViews.all_rooms_view,name="All rooms"),
    path("operations",inventoryViews.all_operations_view,name="All operations"),
    path("loans",inventoryViews.all_loans_view,name="All loans"),

]
