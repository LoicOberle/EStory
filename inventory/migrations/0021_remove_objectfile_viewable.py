# Generated by Django 5.1.1 on 2024-09-21 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0020_room_viewable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='objectfile',
            name='viewable',
        ),
    ]
