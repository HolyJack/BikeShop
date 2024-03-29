from rest_framework.permissions import BasePermission

class IsCartOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user_id == request.user

class IsCartItemOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.cart_id.user_id == request.user

        