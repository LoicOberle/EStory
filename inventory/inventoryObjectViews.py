from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect,JsonResponse
from . import models
from . import utilities
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
    if("inventoryId" in form):
        inventoryId=form["inventoryId"]
        #Comparing inventory ids
        if(objectToModify.inventoryId != inventoryId):
            #Keeping old value to save it in the history change
            oldvalue=objectToModify.inventoryId
            #Changing fields's value
            objectToModify.inventoryId=inventoryId

            #Adding change to history table
            models.ChangeHistory.objects.create(inventoryObject=objectToModify,modifiedBy=request.user,modifiedAt=datetime.now(),fieldName="inventoryId",oldValue=oldvalue,newValue=inventoryId)

    if("name" in form):
        name=form["name"]
        #Comparing names
        if(objectToModify.name != name):
            #Keeping old value to save it in the history change
            oldvalue=objectToModify.name
            #Changing fields's value
            objectToModify.name=name

            #Adding change to history table
            models.ChangeHistory.objects.create(inventoryObject=objectToModify,modifiedBy=request.user,modifiedAt=datetime.now(),fieldName="name",oldValue=oldvalue,newValue=name)

    if("origin" in form):
        origin=form["origin"]
          #Comparing origins
        if(objectToModify.origin != origin):
            #Keeping old value to save it in the history change
            oldvalue=objectToModify.origin
            #Changing fields's value
            objectToModify.origin=origin

            #Adding change to history table
            models.ChangeHistory.objects.create(inventoryObject=objectToModify,modifiedBy=request.user,modifiedAt=datetime.now(),fieldName="origin",oldValue=oldvalue,newValue=origin)

    if("dating" in form):
        dating=form["dating"]
          #Comparing datings
        if(objectToModify.dating != dating):
            #Keeping old value to save it in the history change
            oldvalue=objectToModify.dating
            #Changing fields's value
            objectToModify.dating=dating

            #Adding change to history table
            models.ChangeHistory.objects.create(inventoryObject=objectToModify,modifiedBy=request.user,modifiedAt=datetime.now(),fieldName="dating",oldValue=oldvalue,newValue=dating)

    if("provenance" in form):
        provenance=form["provenance"]
        #Comparing provenances
        if(objectToModify.provenance != provenance):
            #Keeping old value to save it in the history change
            oldvalue=objectToModify.provenance
            #Changing fields's value
            objectToModify.provenance=provenance

            #Adding change to history table
            models.ChangeHistory.objects.create(inventoryObject=objectToModify,modifiedBy=request.user,modifiedAt=datetime.now(),fieldName="provenance",oldValue=oldvalue,newValue=provenance)

    if("reservelocation" in form):
        reservelocation=form["reservelocation"]
         #Comparing reserve locations
        if(objectToModify.reservelocation != reservelocation):
            #Keeping old value to save it in the history change
            oldvalue=objectToModify.reservelocation
            #Changing fields's value
            objectToModify.reservelocation=reservelocation

            #Adding change to history table
            models.ChangeHistory.objects.create(inventoryObject=objectToModify,modifiedBy=request.user,modifiedAt=datetime.now(),fieldName="reservelocation",oldValue=oldvalue,newValue=reservelocation)

    if("author" in form):
        author=form["author"]
         #Comparing authors
        if(objectToModify.author != author):
            #Keeping old value to save it in the history change
            oldvalue=objectToModify.author
            #Changing fields's value
            objectToModify.author=author

            #Adding change to history table
            models.ChangeHistory.objects.create(inventoryObject=objectToModify,modifiedBy=request.user,modifiedAt=datetime.now(),fieldName="author",oldValue=oldvalue,newValue=author)

    if("categories" in form):
       
        if(form["categories"]==""):
            categories="[]"
        else:
            categories=form["categories"]
        categories=json.loads(categories)
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
        utilities.purgeCategories()

    if("materials" in form):
        if(form["materials"]==""):
            materials="[]"
        else:
            materials=form["materials"]
        materials=json.loads(materials)
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
        utilities.purgeMaterials()

    if("description" in form):
        description=form["description"]

        #Comparing descriptions
        if(objectToModify.description != description):
            #Keeping old value to save it in the history change
            oldvalue=objectToModify.description
            #Changing fields's value
            objectToModify.description=description

            #Adding change to history table
            models.ChangeHistory.objects.create(inventoryObject=objectToModify,modifiedBy=request.user,modifiedAt=datetime.now(),fieldName="description",oldValue=oldvalue,newValue=description)

    if("bibliography" in form):
        bibliography=form["bibliography"]
         #Comparing bibliographies
        if(objectToModify.bibliography != bibliography):
            #Keeping old value to save it in the history change
            oldvalue=objectToModify.bibliography
            #Changing fields's value
            objectToModify.bibliography=bibliography

            #Adding change to history table
            models.ChangeHistory.objects.create(inventoryObject=objectToModify,modifiedBy=request.user,modifiedAt=datetime.now(),fieldName="bibliography",oldValue=oldvalue,newValue=bibliography)
 
    if("room" in form):
        room=form["room"]
           #Comparing rooms
        if(room=="-1"):
            room=None

        if(objectToModify.room != room):
            #Keeping old value to save it in the history change

            oldvalue=objectToModify.room
            #Changing fields's value
           
            if(room is not None):
                room=models.Room.objects.get(id=room)
            objectToModify.room=room

            #Adding change to history table
            models.ChangeHistory.objects.create(inventoryObject=objectToModify,modifiedBy=request.user,modifiedAt=datetime.now(),fieldName="room",oldValue=str(oldvalue),newValue=str(room))

    if("thumbnail" in form):
        thumbnail=form["thumbnail"]
        # We don't compare photos, we just clear them and
    
        if(thumbnail): # if we have a thumbnail, we have images                                                                                                                                                                 )
            #Clearing the images
            files=request.FILES
        
            
            objectToModify.photos.clear()
            for index,(k, v) in enumerate(files.items()) :
            
            
                newPhoto=models.ObjectPhoto.objects.create(legend=form[f"photo-legend-{index}"],description=form[f"photo-description-{index}"])
            
                if(int(thumbnail)==int(index)):
                
                    newPhoto.thumbnail=True
                else:
                
                    newPhoto.thumbnail=False
                newPhoto.image.save(v.name,v)
                newPhoto.save()
                
                objectToModify.photos.add(newPhoto)

           
              

             #Clean unused images
           
            utilities.purgeImages()
   
    objectToModify.save()
 


    return HttpResponseRedirect(f"/member/inventory/object/{objectId}/detail/")

