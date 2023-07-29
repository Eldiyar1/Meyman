from rest_framework.permissions import BasePermission as TwoBasePermisson, SAFE_METHODS


class IsAdminUserOrReadOnly(TwoBasePermisson):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_staff
