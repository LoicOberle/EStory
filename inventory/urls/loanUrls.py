from django.contrib import admin
from django.urls import path,include
from ..views import loanViews

urlpatterns = [

    path("<objectId>/all",loanViews.all_loans_view,name="All loans"),
]