from .. import models
from .. import serializers
from django.http import JsonResponse


def all_changes_view(request,objectId,field):
    objectToSearch=models.InventoryObject.objects.get(id=objectId)
    changes=models.ChangeHistory.objects.order_by('modifiedAt').filter(inventoryObject=objectToSearch,fieldName=field).all()
    serializer=serializers.ChangeHistorySerializer(changes,many=True)

    return JsonResponse(serializer.data,safe=False)