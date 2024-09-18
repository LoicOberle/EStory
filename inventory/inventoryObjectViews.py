from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect,JsonResponse
from . import models
from datetime import datetime
import json
import io
def detail_view(request,objectId):

    context={
        "object":models.InventoryObject.objects.get(id=objectId)
    }
    return TemplateResponse(request, 'inventory/pages/objectDetail.html', context=context)

def detail_save(request,objectId):
    #Get object to compare fields
    objectToModify=models.InventoryObject.objects.prefetch_related('categories').prefetch_related('materials').get(id=objectId)

    #Get fields from the form
    form=request.POST
    inventoryId=form["inventoryId"]
    name=form["name"]
    origin=form["origin"]
    dating=form["dating"]
    provenance=form["provenance"]
    reservelocation=form["reservelocation"]
    author=form["author"]
    categories=json.loads(form["categories"])
    materials=json.loads(form["materials"])
    description=form["description"]
    bibliography=form["bibliography"]
    room=form["room"]
    #thumbnail=form["thumbnail"]
    if("thumbnail" in form):
        thumbnail=form["thumbnail"]

              
    #Compare fields and change them if necessary logging it in the history table

    #Comparing inventory ids
    if(objectToModify.inventoryId != inventoryId):
        #Keeping old value to save it in the history change
        oldvalue=objectToModify.inventoryId
        #Changing fields's value
        objectToModify.inventoryId=inventoryId

        #Adding change to history table
        models.ChangeHistory.objects.create(inventoryObject=objectToModify,modifiedBy=request.user,modifiedAt=datetime.now(),fieldName="inventoryId",oldValue=oldvalue,newValue=inventoryId)

    #Comparing names
    if(objectToModify.name != name):
        #Keeping old value to save it in the history change
        oldvalue=objectToModify.name
        #Changing fields's value
        objectToModify.name=name

        #Adding change to history table
        models.ChangeHistory.objects.create(inventoryObject=objectToModify,modifiedBy=request.user,modifiedAt=datetime.now(),fieldName="name",oldValue=oldvalue,newValue=name)


    #Comparing origins
    if(objectToModify.origin != origin):
        #Keeping old value to save it in the history change
        oldvalue=objectToModify.origin
        #Changing fields's value
        objectToModify.origin=origin

        #Adding change to history table
        models.ChangeHistory.objects.create(inventoryObject=objectToModify,modifiedBy=request.user,modifiedAt=datetime.now(),fieldName="origin",oldValue=oldvalue,newValue=origin)

    #Comparing datings
    if(objectToModify.dating != dating):
        #Keeping old value to save it in the history change
        oldvalue=objectToModify.dating
        #Changing fields's value
        objectToModify.dating=dating

        #Adding change to history table
        models.ChangeHistory.objects.create(inventoryObject=objectToModify,modifiedBy=request.user,modifiedAt=datetime.now(),fieldName="dating",oldValue=oldvalue,newValue=dating)

    #Comparing provenances
    if(objectToModify.provenance != provenance):
        #Keeping old value to save it in the history change
        oldvalue=objectToModify.provenance
        #Changing fields's value
        objectToModify.provenance=provenance

        #Adding change to history table
        models.ChangeHistory.objects.create(inventoryObject=objectToModify,modifiedBy=request.user,modifiedAt=datetime.now(),fieldName="provenance",oldValue=oldvalue,newValue=provenance)

    #Comparing reserve locations
    if(objectToModify.reservelocation != reservelocation):
        #Keeping old value to save it in the history change
        oldvalue=objectToModify.reservelocation
        #Changing fields's value
        objectToModify.reservelocation=reservelocation

        #Adding change to history table
        models.ChangeHistory.objects.create(inventoryObject=objectToModify,modifiedBy=request.user,modifiedAt=datetime.now(),fieldName="reservelocation",oldValue=oldvalue,newValue=reservelocation)

    #Comparing authors
    if(objectToModify.author != author):
        #Keeping old value to save it in the history change
        oldvalue=objectToModify.author
        #Changing fields's value
        objectToModify.author=author

        #Adding change to history table
        models.ChangeHistory.objects.create(inventoryObject=objectToModify,modifiedBy=request.user,modifiedAt=datetime.now(),fieldName="author",oldValue=oldvalue,newValue=author)

    #Comparing categories
    objectCategoriesList=[{"id": category.id, "value": category.name} for category in objectToModify.categories.all()]
    
    # Convert both lists to sets of tuples for comparison
    mainCondition=False

    #Check if they all have an id, if not one is obviously new
    pretest=True
    for category in categories:
        if "id" not in category:
            pretest=False

    if(pretest):
        list_set = set((d["id"], d["value"]) for d in categories)
        queryset_set = set((d["id"], d["value"]) for d in objectCategoriesList)
        mainCondition=list_set != queryset_set
    else:
        mainCondition=True


    if(mainCondition):
        #Keeping old value to save it in the history change
        oldvalue=objectCategoriesList
        #Changing fields's value
        objectToModify.categories.clear()
        for category in categories:
            if "id" in category:
                try:
                    newCategory=models.ObjectCategory.objects.get(id=category["id"])
                except models.ObjectCategory.DoesNotExist:
                    return JsonResponse({"error": f"Category with ID {category['id']}"})
            else:
                newCategory=models.ObjectCategory.objects.create(name=category["value"])

            objectToModify.categories.add(newCategory)


        #Adding change to history table
        models.ChangeHistory.objects.create(inventoryObject=objectToModify,modifiedBy=request.user,modifiedAt=datetime.now(),fieldName="categories",oldValue=json.dumps(oldvalue),newValue=json.dumps(categories))


    #Comparing materials
    objectMaterialsList=[{"id": material.id, "value": material.name} for material in objectToModify.materials.all()]
    
    # Convert both lists to sets of tuples for comparison
    mainCondition=False

    #Check if they all have an id, if not one is obviously new
    pretest=True
    for material in materials:
        if "id" not in material:
            pretest=False

    if(pretest):
        list_set = set((d["id"], d["value"]) for d in materials)
        queryset_set = set((d["id"], d["value"]) for d in objectMaterialsList)
        mainCondition=list_set != queryset_set
    else:
        mainCondition=True


    if(mainCondition):
        #Keeping old value to save it in the history change
        oldvalue=objectMaterialsList
        #Changing fields's value
        objectToModify.materials.clear()
        for material in materials:
            if "id" in material:
                try:
                    newMaterial=models.ObjectMaterial.objects.get(id=material["id"])
                except models.ObjectMaterial.DoesNotExist:
                    return JsonResponse({"error": f"Material with ID {material['id']}"})
            else:
                newMaterial=models.ObjectMaterial.objects.create(name=material["value"])

            objectToModify.materials.add(newMaterial)


        #Adding change to history table
        models.ChangeHistory.objects.create(inventoryObject=objectToModify,modifiedBy=request.user,modifiedAt=datetime.now(),fieldName="materials",oldValue=json.dumps(oldvalue),newValue=json.dumps(materials))


    #Comparing descriptions
    if(objectToModify.description != description):
        #Keeping old value to save it in the history change
        oldvalue=objectToModify.description
        #Changing fields's value
        objectToModify.description=description

        #Adding change to history table
        models.ChangeHistory.objects.create(inventoryObject=objectToModify,modifiedBy=request.user,modifiedAt=datetime.now(),fieldName="description",oldValue=oldvalue,newValue=description)

    #Comparing bibliographies
    if(objectToModify.bibliography != bibliography):
        #Keeping old value to save it in the history change
        oldvalue=objectToModify.bibliography
        #Changing fields's value
        objectToModify.bibliography=bibliography

        #Adding change to history table
        models.ChangeHistory.objects.create(inventoryObject=objectToModify,modifiedBy=request.user,modifiedAt=datetime.now(),fieldName="bibliography",oldValue=oldvalue,newValue=bibliography)

    #Comparing rooms
    if(room=="-1"):
        room=None

    if(objectToModify.room != room):
        #Keeping old value to save it in the history change

        oldvalue=objectToModify.room
        #Changing fields's value
        print(room)
        if(room is not None):
            room=models.Room.objects.get(id=room)
        objectToModify.room=room

        #Adding change to history table
        models.ChangeHistory.objects.create(inventoryObject=objectToModify,modifiedBy=request.user,modifiedAt=datetime.now(),fieldName="room",oldValue=str(oldvalue),newValue=str(room))



    # We don't compare photos, we just clear them and
    print(request.FILES)
    if(thumbnail): # if we have a thumbnail, we have images                                                                                                                                                                 )
        #Clearing the images
        files=request.FILES
    
        
        objectToModify.photos.clear()
        for index,(k, v) in enumerate(files.items()) :
           
           
            newPhoto=models.ObjectPhoto.objects.create(legend=form[f"photo-legend-{index}"],description=form[f"photo-description-{index}"])
            print(index)
            print(thumbnail)
            if(int(thumbnail)==int(index)):
                print("it is a thumbnail")
                newPhoto.thumbnail=True
            else:
                print("it is not a thumbnail",int(index),int(thumbnail))
                newPhoto.thumbnail=False
            newPhoto.image.save(v.name,v)
            newPhoto.save()
            print(newPhoto.thumbnail)
            objectToModify.photos.add(newPhoto)

    print(objectToModify.photos.all())
                                    
    #We loop the images without an object to delete them

    related_ids = models.InventoryObject.objects.values('photos')

    unrelated_ids = models.ObjectPhoto.objects.exclude(id__in=related_ids).delete()

    objectToModify.save()
 


    return HttpResponseRedirect(f"/member/inventory/object/{objectId}/detail/")