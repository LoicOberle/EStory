from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect,JsonResponse,HttpResponse
from .. import models
from .. import utilities
from .. import serializers
from datetime import datetime
import json
import io
def detail_view(request,objectId):

    context={
        "object":models.InventoryObject.objects.get(id=objectId)
    }
    return TemplateResponse(request, 'inventory/pages/objectDetail.html', context=context)

def infos_save(request,objectId):
    #Get object to compare fields
    objectToModify=models.InventoryObject.objects.prefetch_related('categories').prefetch_related('materials').get(id=objectId)

    #Get fields from the form
    form=request.POST
    postFiles=request.FILES

    if("viewable" in form):
        print(form["viewable"])
        objectToModify.viewable=True
    else:
         objectToModify.viewable=False

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


    for photoToDelete in objectToModify.photos.all():
        photoToDelete.delete()

    objectToModify.photos.clear()
    if("thumbnail" in form):
        thumbnail=form["thumbnail"]
        # We don't compare photos, we just clear them and
     
        if(thumbnail): # if we have a thumbnail, we have images                                                                                                                                                                 )
            #Clearing the images
           
            

            #Getting list of photos
            photos=[]
            for index,(k, v) in enumerate(postFiles.items()) :
                if("photos" in k):
                    photos.append((k,v))
            for index,(k, v) in enumerate(photos) :
                viewable=False
                if(f"photo-viewable-{index}" in form):
                    viewable=True
            
                newPhoto=models.ObjectPhoto.objects.create(legend=form[f"photo-legend-{index}"],description=form[f"photo-description-{index}"],viewable=viewable)
            
                if(int(thumbnail)==int(index)):
                
                    newPhoto.thumbnail=True
                else:
                
                    newPhoto.thumbnail=False
                newPhoto.image.save(v.name,v)
                newPhoto.save()
                
                objectToModify.photos.add(newPhoto)

             #Clean unused images
           
            utilities.purgeImages()

    # We don't compare files, we just clear them and add new ones
    for fileToDelete in objectToModify.files.all():
        fileToDelete.delete()
    objectToModify.files.clear()

    #Getting list of files
    files=[]
    for index,(k, v) in enumerate(postFiles.items()) :
        if("files" in k):
            files.append((k,v))

  
    for index,(k, v) in enumerate(files) :
        viewable=False
        if(f"file-viewable-{index}" in form):
            viewable=True

        newFile=models.ObjectFile.objects.create(name=form[f"file-name-{index}"],viewable=viewable)
    
        newFile.file.save(v.name,v)
        newFile.save()
        
        objectToModify.files.add(newFile)

    #Clean unused images
    
    utilities.purgeFiles()
   
    objectToModify.save()
 


    return HttpResponseRedirect(f"/member/inventory/object/{objectId}/detail/")

def operations_save(request,objectId):
    form=request.POST
    operationDatetime=form["datetime"]
    operationDescription=form["description"]
    objectToModify=models.InventoryObject.objects.get(id=objectId)

    print(operationDatetime)
    formattedOperationDatetime=datetime.strptime(operationDatetime, "%Y-%m-%d %H:%M") #'2024-09-18 12:00'
    
    models.OperationHistory.objects.create(inventoryObject=objectToModify,date=formattedOperationDatetime,description=operationDescription,author=request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def loans_save(request,objectId):
    form=request.POST
    print(form)
    loanStartDate=form["startDate"]
    loanEndDate=form["endDate"]
    if("ongoing" in form):
        loanOngoing=True
    else:
        loanOngoing=False

    loanDescription=form["description"]
    objectToModify=models.InventoryObject.objects.get(id=objectId)

    newLoan=models.LoanHistory.objects.create(inventoryObject=objectToModify,description=loanDescription,ongoing=loanOngoing)
    
    if(loanStartDate != ""):
        formattedLoanStartDate=datetime.strptime(loanStartDate, "%Y-%m-%d") #'2024-09-18 12:00'
        newLoan.startDate=formattedLoanStartDate
    if(loanEndDate != ""):   
        formattedLoanEndDate=datetime.strptime(loanEndDate, "%Y-%m-%d") #'2024-09-18 12:00'
        newLoan.endDate=formattedLoanEndDate
    
    newLoan.save()
    
  

       
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def loans_edit(request,objectId):
    form=request.POST
    print(form)
    loanStartDate=form["startDate"]
    loanEndDate=form["endDate"]
    if("ongoing" in form):
        loanOngoing=True
    else:
        loanOngoing=False
    loanDescription=form["description"]

    loanToModify=models.LoanHistory.objects.get(id=form["loanId"])

    if(loanStartDate != ""):
        formattedLoanStartDate=datetime.strptime(loanStartDate, "%Y-%m-%d") #'2024-09-18 12:00'
        loanToModify.startDate=formattedLoanStartDate
    if(loanEndDate != ""):
        formattedLoanEndDate=datetime.strptime(loanEndDate, "%Y-%m-%d") #'2024-09-18 12:00'
        loanToModify.endDate=formattedLoanEndDate
    

    loanToModify.ongoing=loanOngoing
    loanToModify.description=loanDescription     
    
    loanToModify.save()
 
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


###########################################################################3



def all_objects_view(request):
    user_groups = request.user.groups.all()
    if(len(user_groups)>0 and not request.user.is_superuser): #If a user has a group we only get the object of the same group, otherwise we get them all
        objects = models.InventoryObject.objects.filter(createdBy__groups__in=user_groups).distinct()
        serializer=serializers.InventoryObjectSerializer(objects,many=True)
        ownership=[]
        for object in serializer.data:
    
            canDelete=(object["createdBy"]["id"]==request.user.id or request.user.is_superuser)
            ownership.append(canDelete)
    else:
        objects=models.InventoryObject.objects.all()
        serializer=serializers.InventoryObjectSerializer(objects,many=True)
        ownership=[]
        for object in serializer.data:
            ownership.append(True)
     
    
   
    
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