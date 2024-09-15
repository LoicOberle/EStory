from django.db import models
from django.contrib.auth.models import User
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
    legend=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.legend
    


#Define an inventory object
class InventoryObject(models.Model):
    inventoryId=models.CharField(max_length=100)
    categories=models.ManyToManyField(ObjectCategory,blank=True)
    materials=models.ManyToManyField(ObjectMaterial,blank=True)
    photos=models.ManyToManyField(ObjectPhoto,blank=True)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
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
    


