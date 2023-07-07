from rest_framework.permissions import BasePermission, SAFE_METHODS


class AllowAnyReadOnlyOrStaff(BasePermission):
    def has_permission(self, request, view):
        # Allow all GET, HEAD, OPTIONS requests (read-only) for anonymous users
        if request.method in SAFE_METHODS:
            return True
        
        # Allow unrestricted access to admin users
        return request.user.is_staff