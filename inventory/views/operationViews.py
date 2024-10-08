from .. import models
from .. import serializers
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


def all_operations_view(request,objectId):
    objectToSearch=models.InventoryObject.objects.get(id=objectId)
    operations=models.OperationHistory.objects.order_by('date').filter(inventoryObject=objectToSearch).all()
    serializer=serializers.OperationHistorySerializer(operations,many=True)

    return JsonResponse(serializer.data,safe=False)