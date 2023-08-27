from rest_framework.permissions import BasePermission


class OwnerPermission(BasePermission):
    """ Класс для определения владельца """
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
