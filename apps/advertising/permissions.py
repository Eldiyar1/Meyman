from rest_framework.permissions import BasePermission as FourBasePermission, SAFE_METHODS

class IsAdminOrReadOnly(FourBasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_staff