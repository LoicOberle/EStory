# Generated by Django 5.1.1 on 2024-09-21 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0016_alter_objectfile_viewable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryobject',
            name='viewable',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
