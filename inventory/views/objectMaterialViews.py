from .. import models
from .. import serializers
from django.http import JsonResponse

def all_materials_view(request):
    materials=models.ObjectMaterial.objects.all()
    serializer=serializers.ObjectMaterialSerializer(materials,many=True)
    return JsonResponse(serializer.data,safe=False)