import re

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user


def removeHTML(value):
    dr = re.compile(r'<[^>]+>', re.S)
    dd = dr.sub('', value)
    return dd
