from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.InventoryObject)
admin.site.register(models.ObjectCategory)
admin.site.register(models.ObjectMaterial)
admin.site.register(models.ObjectPhoto)
admin.site.register(models.ObjectFile)
admin.site.register(models.ChangeHistory)
admin.site.register(models.Room)
admin.site.register(models.LoanHistory)
admin.site.register(models.OperationHistory)