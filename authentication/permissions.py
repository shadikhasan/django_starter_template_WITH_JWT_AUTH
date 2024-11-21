from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin'

class IsMemberUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'member'
