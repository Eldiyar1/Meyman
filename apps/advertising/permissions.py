from rest_framework.permissions import BasePermission

class IsUnregistered(BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_authenticated