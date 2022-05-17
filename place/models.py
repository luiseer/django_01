from django.db import models
import uuid
from vehicle.models import Vehicle
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    @property
    def name_address(self) -> str:
        return f"{self.name} | {self.address}"
    
class Rack(models.Model):
    number = models.IntegerField(null = False, unique=True)
    uuid = models.UUIDField(default=uuid.uuid4())
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.place.id} | {self.number}"
    
    @property
    def name_uuid(self)-> dict:
        return{
            "number": self.number,
            "id": self.uuid,
        }


class RackItem(models.Model):
    rack = models.ForeignKey(Rack, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.id}|{self.vehicle.plate}|{self.vehicle.owner.email}"

@receiver(post_save, sender=RackItem)
def update_status_rack(sender, instance, created, **kwargs):
    if created:
        rack_item = instance
        rack_id = rack_item.rack.id
        rack = Rack.objects.get(id=rack_id)
        rack.statu = False
        rack.save()

@receiver(post_delete, sender=RackItem)
def update_status_rack_delete(sender, instance, **kwargs):
    rack_item = instance
    rack_id = rack_item.rack.id
    rack = Rack.objects.get(id=rack_id)
    rack.statu = True
    rack.save()