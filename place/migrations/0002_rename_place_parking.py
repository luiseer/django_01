# Generated by Django 3.2.13 on 2022-05-17 16:54

from django.db import migrations


class Migration(migrations.Migration):
    
    atomic = False 

    dependencies = [
        ('place', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Place',
            new_name='Parking',
        ),
    ]
