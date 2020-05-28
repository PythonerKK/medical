import re

from django.http import JsonResponse
from rest_framework import permissions

from utils.response_code import ResponseCode


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user


def removeHTML(value):
    dr = re.compile(r'<[^>]+>', re.S)
    dd = dr.sub('', value)
    return dd


def response_success():
    return JsonResponse({"code": "200", "message": "ok"})

def response_success_with_data(data):
    return JsonResponse({"code": "200", "message": "ok", "data": data})

def response_fail(message):
    return JsonResponse({"code": "500", "message": message})
