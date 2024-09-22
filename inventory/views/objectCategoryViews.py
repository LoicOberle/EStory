from .. import models
from .. import serializers
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from urllib.parse import urlparse

def all_categories_view(request):
    categories=models.ObjectCategory.objects.all()
    serializer = serializers.ObjectCategorySerializer(categories,many=True)
    return JsonResponse(serializer.data,safe=False)