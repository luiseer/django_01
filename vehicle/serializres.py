from rest_framework import serializers
from .models import Vehicle

class VehicleSerilizer(serializers.ModelSerializer):
    vehicle = serializers.CharField(source="get_vehicle.display")
    class Meta:
        model = Vehicle
        fields = "__all__"
        