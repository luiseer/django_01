# Generated by Django 3.2 on 2022-05-18 03:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0015_alter_rack_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rack',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('a0c9df63-8cb2-4485-9d03-d280505f5f8d')),
        ),
    ]
