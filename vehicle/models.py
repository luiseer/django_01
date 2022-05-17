from django.db import models
from core.models import User

# Create your models here.

class Vehicle(models.Model):
    VEHICLES_CHOICES = [
        ('C', 'Car'),
        ('M', 'Motorcycle'),
        ('B', 'Bicycle'),
    ]
    ENGINE_CHOISES = [
        ('c', 'Combustion'),
        ('e', 'Electric'),
    ]
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.CharField(max_length=1, choices=VEHICLES_CHOICES)
    plate = models.CharField(max_length=10, unique=True)
    color = models.CharField(max_length=10)
    engine = models.CharField(max_length=1, choices=ENGINE_CHOISES, blank=True, null=True)
    
    def __str__(self):
        return f"{self.owner.email} | {self.plate} | {self.vehicle}"