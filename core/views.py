from argparse import Action
from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from .permissions import IsOwnerOrReadOnly
from vehicle.models import Vehicle
from vehicle.serializres import VehicleSerilizer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

# Create your views here


class UserViewSet(viewsets.ModelViewSet):
     queryset = User.objects.all()
     serializer_class = UserSerializer
     permission_classes = [IsAuthenticated]
     
     def get_permissions(self):
          if self.action == 'create':
               permission_classes = [AllowAny]
          else:
               permission_classes = [IsOwnerOrReadOnly]
     
          return [permissions() for permissions in permission_classes]

@action(detail = True)
def my_cars(self, request, pk=None):
     queryset = Vehicle.objects.filter(
          owner__id = pk
     )
     serializer = VehicleSerilizer(queryset, many=True)
     return Response(serializer.data, status=status.HTTP_200_OK )