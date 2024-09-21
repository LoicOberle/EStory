from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponse,JsonResponse
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.models import Group
import json
from inventory import models
from inventory import serializers

def all_objects_view(request):
    user_groups = request.user.groups.all()
    if(request.user.is_authenticated and len(user_groups)>0 and not request.user.is_superuser): #If a user has a group we only get the object of the same group, otherwise we get them all
        objects = models.InventoryObject.objects.filter(createdBy__groups__in=user_groups).distinct()
    else:
        objects=models.InventoryObject.objects.all()
     
    serializer=serializers.InventoryObjectSerializer(objects,many=True)
   
    ownership=[]
    for object in serializer.data:
 
        canDelete=(object["createdBy"]["id"]==request.user.id or request.user.is_superuser)
        ownership.append(canDelete)
    return JsonResponse({"data": serializer.data,"ownership":ownership},safe=False)

def new_object_view(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    inventoryId = body['inventoryId']
    
    newObject=models.InventoryObject.objects.create(inventoryId=inventoryId,createdBy=request.user)
    serializer=serializers.InventoryObjectSerializer(newObject)
    return JsonResponse(serializer.data,safe=False)

def object_view(request,objectId):
    object=models.InventoryObject.objects.prefetch_related('categories').prefetch_related('materials').prefetch_related('photos').get(id=objectId)
   
    serializer=serializers.InventoryObjectSerializer(object)
  
                                                                                                     
    return JsonResponse(serializer.data,safe=False)    

def object_delete(request,objectId):
    object=models.InventoryObject.objects.get(id=objectId)
    object.delete()
                                                                                              
    return JsonResponse({},safe=False)        

    
def all_categories_view(request):
    categories=models.ObjectCategory.objects.all()
    serializer = serializers.ObjectCategorySerializer(categories,many=True)
    return JsonResponse(serializer.data,safe=False)

def all_materials_view(request):
    materials=models.ObjectMaterial.objects.all()
    serializer=serializers.ObjectMaterialSerializer(materials,many=True)
    return JsonResponse(serializer.data,safe=False)

def all_rooms_view(request):
    rooms=models.Room.objects.all()
    roomsList=serializers.RoomSerializer(rooms,many=True).data
    roomsList.append({
        "id":-1,
        "name":"Unlisted"
    })
    return JsonResponse(roomsList,safe=False)

def all_groups_view(request):
    groups=Group.objects.all().values()
  

    groupList=serializers.GroupSerializer(groups,many=True).data

    return JsonResponse(groupList,safe=False)

def all_operations_view(request,objectId):
    objectToSearch=models.InventoryObject.objects.get(id=objectId)
    operations=models.OperationHistory.objects.order_by('date').filter(inventoryObject=objectToSearch).all()
    serializer=serializers.OperationHistorySerializer(operations,many=True)

    return JsonResponse(serializer.data,safe=False)

def all_loans_view(request,objectId):
    objectToSearch=models.InventoryObject.objects.get(id=objectId)
    loans=models.LoanHistory.objects.order_by('startDate').filter(inventoryObject=objectToSearch).all()
    serializer=serializers.LoanHistorySerializer(loans,many=True)

    return JsonResponse(serializer.data,safe=False)


def all_changes_view(request,objectId,field):
    objectToSearch=models.InventoryObject.objects.get(id=objectId)
    changes=models.ChangeHistory.objects.order_by('modifiedAt').filter(inventoryObject=objectToSearch,fieldName=field).all()
    serializer=serializers.ChangeHistorySerializer(changes,many=True)

    return JsonResponse(serializer.data,safe=False)