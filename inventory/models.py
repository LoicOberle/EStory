from django.db import models
from django.contrib.auth.models import User
import os
#Define materials an object can be made of
class ObjectMaterial(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    

#Define categories an object can have
class ObjectCategory(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name

#Define photos that can be associated with an object
class ObjectPhoto(models.Model):
    legend=models.CharField(max_length=100,blank=True)
    description=models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    thumbnail=models.BooleanField(default=False,null=True,blank=True)
    viewable=models.BooleanField(null=True,blank=True,default=True)
    def __str__(self):
        return self.legend
    def delete(self, *args, **kwargs):
        # Delete the file associated with this instance
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)

        # Call the superclass's delete method to delete the instance
        super().delete(*args, **kwargs)

class ObjectFile(models.Model):
    name=models.CharField(max_length=100,blank=True)
    file=models.FileField(upload_to="files/")
    viewable=models.BooleanField(null=True,blank=True,default=False)

    
#Define a room of the museum
class Room(models.Model):
    name=models.CharField(max_length=255,blank=True)

#Define an inventory object
class InventoryObject(models.Model):
    inventoryId=models.CharField(max_length=100)
    categories=models.ManyToManyField(ObjectCategory,blank=True)
    materials=models.ManyToManyField(ObjectMaterial,blank=True)
    photos=models.ManyToManyField(ObjectPhoto,blank=True)
    files=models.ManyToManyField(ObjectFile,blank=True)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=255,blank=True)
    description=models.TextField(blank=True)
    origin=models.CharField(max_length=200,blank=True)
    dating=models.CharField(max_length=200,blank=True)
    provenance=models.CharField(max_length=100,blank=True)
    reservelocation=models.CharField(max_length=100,blank=True)
    author=models.CharField(max_length=100,blank=True)
    bibliography=models.TextField(default="",blank=True)
    room=models.ForeignKey(Room,null=True,on_delete=models.SET_NULL,blank=True)
    viewable=models.BooleanField(null=True,blank=True,default=False)
    def __str__(self):
        return self.inventoryId



#Define the change history of an object's fields
class ChangeHistory(models.Model):
    inventoryObject = models.ForeignKey(InventoryObject,on_delete=models.CASCADE)
    modifiedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    modifiedAt = models.DateTimeField(auto_now_add=True)
    fieldName=models.CharField(max_length=100)
    oldValue=models.TextField()
    newValue=models.TextField()
    def __str__(self):
        return f"Change of {self.inventoryObject} by {self.modifiedBy} at {self.modifiedAt} on {self.fieldName}"
    


#Define the loan history of an object
class LoanHistory(models.Model):
    inventoryObject=models.ForeignKey(InventoryObject,on_delete=models.CASCADE) 
    startDate=models.DateField(blank=True,null=True)
    endDate=models.DateField(blank=True,null=True)
    ongoing=models.BooleanField(blank=True,null=True)
    description=models.TextField(blank=True,null=True)

#Define the operation history of an object
class OperationHistory(models.Model):
    inventoryObject=models.ForeignKey(InventoryObject,on_delete=models.CASCADE) 
    date=models.DateTimeField(blank=True,null=True)
    description=models.TextField()
    author=models.ForeignKey(User, on_delete=models.CASCADE)