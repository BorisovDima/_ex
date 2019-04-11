from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from .permissions import InRoomPermission
from chat.apps.core.endpoints import AsyncAPI
from django.views.generic import TemplateView

from rest_framework.decorators import action
from channels.layers import get_channel_layer

from .serializer import  MessageSerializer, RoomSerializer
from .models import Room, Message



class EventGroupAPI(AsyncAPI):
    permission_classes = (IsAuthenticated,)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layer = get_channel_layer()

    def get_channel(self, request):
        return request._request.channel_group, request._request.channel_name

    async def delete(self, request, *args, **kwargs):
        group, name = self.get_channel(request)
        await self.layer.group_discard(group, name)
        print('User deleted')
        # return Response({},

    async def post(self, request, *args, **kwargs):
        print(request.user)
        group, name = self.get_channel(request)
        print(group, name, '!!!!!!!!!!!!!!!!!!!!!!!!! NMAE')
        await self.layer.group_add(group, name)
        await self.layer.group_discard('unauthorized', name)
        return Response({}, status=status.HTTP_201_CREATED)



class RoomAPI(ModelViewSet):

    """
    get:
    Return a list of user rooms.

    post:
    Create a new room.
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = RoomSerializer
    obj = property(lambda s: RoomAPI.get_object(s))

    @action(detail=True, methods=['get'], permission_classes=(IsAuthenticated, InRoomPermission,))
    def messages(self, request, **kwargs):
        msgs = self.paginate_queryset(self.obj.get_msgs(request))
        data = MessageSerializer(msgs, many=True, context={'request': request}).data
        return self.get_paginated_response(data)

    @messages.mapping.post
    def messages_create(self, request, **kwargs):
        print(request.data)
        msg = MessageSerializer(data=request.data, context={'request': request})
        msg.is_valid(raise_exception=True)
        msg.save(room=self.obj, author=self.request.user)
        return Response(msg.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'], permission_classes=(IsAuthenticated,))
    def group_create(self, request):
        pass

    @action(detail=True, methods=['patch'], permission_classes=(IsAuthenticated, InRoomPermission))
    def group_add(self, request, **kwargs):
        pass

    def create(self, request, *args, **kwargs):
        id = self.request.data.get('user_id')
        self.user = get_object_or_404(get_user_model(), id=id)
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, user=self.user)

    def get_queryset(self):
        return self.request.user.room_set.all()


class MessageAPI(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    @action(detail=True, methods=['patch'], permission_classes=(IsAuthenticated, InRoomPermission))
    def viewed(self, request, *args, **kwargs):
        msg = self.get_object()
        msg.who_viewed_it.add(request.user)
        return Response({}, status=status.HTTP_200_OK)


class Index(TemplateView):
    template_name = 'index.html'

