from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsrMineOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.user_type == "client"

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
