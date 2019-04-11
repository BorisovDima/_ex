from rest_framework.permissions import BasePermission
from .models import Room, Message

class InRoomPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user in (obj.users.all() if type(obj) == Room else obj.room.users.all())