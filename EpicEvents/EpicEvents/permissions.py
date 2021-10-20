from rest_framework import permissions
from client.models import Client


class IsSale(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        all_clients = Client.objects.all()
        clients = all_clients.filter(sales_contact=request.user)
        if hasattr(obj, 'support_contact'):
            if obj.client in clients:
                return True
        else:
            return obj.sales_contact == request.user


class IsSupport(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'support_contact'):
            return obj.support_contact == request.user


class IsManagement(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff
