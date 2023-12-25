from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdministrator(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_administrator


class IsAdministratorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_administrator or request.method in SAFE_METHODS
