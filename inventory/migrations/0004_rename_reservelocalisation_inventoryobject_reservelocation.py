# Generated by Django 5.1.1 on 2024-09-17 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_alter_inventoryobject_room'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventoryobject',
            old_name='reservelocalisation',
            new_name='reservelocation',
        ),
    ]
