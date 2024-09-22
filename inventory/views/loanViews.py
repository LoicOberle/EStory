from .. import models
from .. import serializers
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
def all_loans_view(request,objectId):
    objectToSearch=models.InventoryObject.objects.get(id=objectId)
    loans=models.LoanHistory.objects.order_by('startDate').filter(inventoryObject=objectToSearch).all()
    serializer=serializers.LoanHistorySerializer(loans,many=True)

    return JsonResponse(serializer.data,safe=False)
