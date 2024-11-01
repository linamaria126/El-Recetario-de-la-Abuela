from rest_framework.permissions import BasePermission

class IsAdminReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method =='GET' or request.method == 'POST':
            return request.user.is_active
        else:
            return request.user.is_staff
            