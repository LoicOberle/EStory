from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponse,JsonResponse
import json
from inventory import models
from inventory import serializers

def all_objects_view(request):
    objects=models.InventoryObject.objects.all().values()
    data=list(objects)
    ownership=[]
    for object in data:
        canDelete=(object["createdBy_id"]==request.user.id or request.user.is_superuser)
        ownership.append(canDelete)
    return JsonResponse({"data": data,"ownership":ownership},safe=False)

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
    categories=models.ObjectCategory.objects.all().values()
    return JsonResponse({"data": list(categories)},safe=False)

def all_materials_view(request):
    materials=models.ObjectMaterial.objects.all().values()
    return JsonResponse({"data": list(materials)},safe=False)

def all_rooms_view(request):
    rooms=models.Room.objects.all().values()
    roomsList=list(rooms)
    roomsList.append({
        "id":-1,
        "name":"Unlisted"
    })
    return JsonResponse({"data": roomsList},safe=False)