from rest_framework.permissions import BasePermission as ThreeBasePermission, SAFE_METHODS


class IsAdminUserOrReadOnly(ThreeBasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_staff
