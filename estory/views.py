from django.template.response import TemplateResponse

import os
from dotenv import load_dotenv

load_dotenv() 


def home_view(request):
 
    context = {
        "name":os.getenv('SITE_NAME'),
        'isUserConnected':request.user.is_authenticated
    }
    return TemplateResponse(request, 'estory/pages/home.html', context=context)