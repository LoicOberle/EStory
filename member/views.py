from django.shortcuts import render
from django.template.response import TemplateResponse

def index_view(request):
 
    context = {
       
    }
    return TemplateResponse(request, 'member/pages/index.html', context=context)