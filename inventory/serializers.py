from rest_framework import serializers
from . import models
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
        fields = ['id','legend','description','image','thumbnail']

class InventoryObjectSerializer(serializers.ModelSerializer):
    categories = ObjectCategorySerializer(many=True)
    materials = ObjectMaterialSerializer(many=True)
    photos = ObjectPhotoSerializer(many=True)
    class Meta:
        model = models.InventoryObject
        fields = ['id',"inventoryId",'name', 'categories','materials','photos','description','createdBy','createdAt','origin','dating','provenance','reservelocation','author','bibliography','room']