from django.shortcuts import render
from django.template.response import TemplateResponse
from .. import models
from django.contrib.auth.decorators import login_required

@login_required
def index_view(request):
 
    context = {
       
    }
    return TemplateResponse(request, 'inventory/pages/index.html', context=context)

@login_required
def object_detail_view(request,objectId):

    context={
        "object":models.InventoryObject.objects.get(id=objectId)
    }
    return TemplateResponse(request, 'inventory/pages/objectDetail.html', context=context)
