# Generated by Django 5.1.1 on 2024-09-19 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_alter_operationhistory_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LendingHistory',
            new_name='LoanHistory',
        ),
    ]
