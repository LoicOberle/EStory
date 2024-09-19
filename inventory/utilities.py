import os
from django.conf import settings
from . import models
def purgeImages():
    #We loop the images without an object to delete them

    related_ids = models.InventoryObject.objects.values('photos')

    unrelated_ids = models.ObjectPhoto.objects.exclude(id__in=related_ids)
    for model in unrelated_ids:
        model.delete()

    # Step 1: Get all image files from the media directory
    media_directory = settings.MEDIA_ROOT
    all_files_in_media = set(
        os.path.join(root, file)
        for root, dirs, files in os.walk(media_directory)
        for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))
    )

    # Step 2: Get all image files currently associated with ImageField in MyModel
    used_images = set(
        os.path.join(settings.MEDIA_ROOT, instance.image.name)
        for instance in models.ObjectPhoto.objects.all()
        if instance.image  # if image field is not empty
    )

    # Step 3: Identify and delete unused images
    unused_images = all_files_in_media - used_images

    for image_path in unused_images:
        os.remove(image_path)

def purgeCategories():
    related_ids = models.InventoryObject.objects.values('categories')

    unrelated_ids = models.ObjectCategory.objects.exclude(id__in=related_ids)

    for model in unrelated_ids:
        model.delete()

def purgeMaterials():
    related_ids = models.InventoryObject.objects.values('materials')

    unrelated_ids = models.ObjectMaterial.objects.exclude(id__in=related_ids)
    for model in unrelated_ids:
        model.delete()