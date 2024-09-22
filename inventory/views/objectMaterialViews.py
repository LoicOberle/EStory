from .. import models
from .. import serializers
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from urllib.parse import urlparse

def all_materials_view(request):
    materials=models.ObjectMaterial.objects.all()
    serializer=serializers.ObjectMaterialSerializer(materials,many=True)
    return JsonResponse(serializer.data,safe=False)