# Generated by Django 3.2 on 2022-05-18 03:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0008_alter_rack_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rack',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='rack',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('f02678a5-bba6-48d3-b232-ac44ea875c6c')),
        ),
    ]