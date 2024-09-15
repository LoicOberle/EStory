from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.InventoryObject)
admin.site.register(models.ObjectCategory)
admin.site.register(models.ObjectMaterial)
admin.site.register(models.ObjectPhoto)
admin.site.register(models.ChangeHistory)