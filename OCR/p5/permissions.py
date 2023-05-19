from rest_framework.permissions import BasePermission

class AllowOnlyPostWithoutAuthentication(BasePermission):
    def has_permission(self, request, view):
        return request.method == 'POST' and not request.user.is_authenticated