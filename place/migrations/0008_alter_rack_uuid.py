# Generated by Django 3.2 on 2022-05-17 23:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0007_alter_rack_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rack',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('11cd4331-9112-4600-8f79-9ea12e16219e')),
        ),
    ]
