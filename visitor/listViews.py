from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponse,JsonResponse

def index_view(request):
    context={
        
    }
    return TemplateResponse(request, 'visitor/list/pages/index.html', context=context)

def object_detail_view(request,objectId):
    context={
        
    }
    return TemplateResponse(request, 'visitor/list/pages/index.html', context=context)