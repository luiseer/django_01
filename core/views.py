from django.shortcuts import render
from .models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsOwnerOrReadOnly
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
             
         return [permission() for permission in permission_classes]