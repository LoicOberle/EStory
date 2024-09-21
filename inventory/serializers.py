from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class ObjectCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ObjectCategory
        fields = ['id','name']

class ObjectMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ObjectMaterial
        fields = ['id','name']

class ObjectPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ObjectPhoto
        fields = ['id','legend','description','image','thumbnail','viewable']

class ObjectFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ObjectFile
        fields = ['id','name','file','viewable']

class InventoryObjectSerializer(serializers.ModelSerializer):
    categories = ObjectCategorySerializer(many=True)
    materials = ObjectMaterialSerializer(many=True)
    photos = ObjectPhotoSerializer(many=True)
    files = ObjectFileSerializer(many=True)
    createdBy=UserSerializer(many=False)
    class Meta:
        model = models.InventoryObject
        fields = ['id',"inventoryId",'name', 'categories','materials','photos','files','description','createdBy','createdAt','origin','dating','provenance','reservelocation','author','bibliography','room','viewable']

class OperationHistorySerializer(serializers.ModelSerializer):
    inventoryObject=InventoryObjectSerializer(many=False)
    author=UserSerializer(many=False)
    class Meta:
        model=models.OperationHistory
        fields=["id","inventoryObject","date","description","author"]
        

class LoanHistorySerializer(serializers.ModelSerializer):
    inventoryObject=InventoryObjectSerializer(many=False)
    class Meta:
        model=models.LoanHistory
        fields=["id","inventoryObject","startDate","description","endDate","ongoing"]

class ChangeHistorySerializer(serializers.ModelSerializer):
    inventoryObject=InventoryObjectSerializer(many=False)
    modifiedBy=UserSerializer(many=False)
    class Meta:
        model=models.ChangeHistory
        fields=["id","inventoryObject","modifiedBy","modifiedAt","fieldName","oldValue","newValue"]
        

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Room
        fields=["id","name"]