from django.contrib import admin
from django.urls import path,include
from ..views import pagesViews

urlpatterns = [
    path("",pagesViews.index_view,name="Index"),
    path("object/",include("inventory.urls.inventoryObjectUrls")),
    path("category/",include("inventory.urls.objectCategoryUrls")),
    path("material/",include("inventory.urls.objectMaterialUrls")),
    path("room/",include("inventory.urls.roomUrls")),
    path("operation/",include("inventory.urls.operationUrls")),
    path("loan/",include("inventory.urls.loanUrls")),
    path("group/",include("inventory.urls.groupUrls")),
    path("change/",include("inventory.urls.changeUrls"))
   
]
