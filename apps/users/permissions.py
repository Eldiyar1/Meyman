from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_staff

class CustomTokenAuthentication(TokenAuthentication):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            raise AuthenticationFailed('You must be authenticated to access this resource.')

        return True
class IsOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return request.user and request.user.is_authenticated and request.user.user_type == 'owner'

class IsClientOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return request.user and request.user.is_authenticated and request.user.user_type == 'client'





