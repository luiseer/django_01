from rest_framework import permissions

<<<<<<< HEAD
class IsOwnerOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if request.user.is_superuser or request.user.is_staff:
            return True
        
        return obj == request.user
=======

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_superuser or request.user.is_staff:
            return True

        return obj.owner == request.user
>>>>>>> 8347742c80d2aadeb0033aa98ac5241fd923aca9
