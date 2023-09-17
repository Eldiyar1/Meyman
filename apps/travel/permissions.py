from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerUserOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user and request.user.is_authenticated and request.user.user_type == "owner"


class IsOwnerUserOrReadOnlyForRooms(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated and request.user.user_type == "owner"


class IsClientUserOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user and request.user.is_authenticated and request.user.user_type == "client"


class IsrMineOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.user_type == "client"

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
