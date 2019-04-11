from django.dispatch import receiver, Signal
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from chat.apps.core.utils import make_response
from rest_framework.response import Response
from rest_framework import status


create = Signal(providing_args=['instance', 'json', 'callback'])


@receiver(create, dispatch_uid='create')
def chat_create(sender, **kwargs):
    callback = kwargs['callback']
    layer = get_channel_layer()
    globals()[callback](layer, **kwargs)


def send_message(layer, callback, **kwargs):
    room = kwargs['instance'].room
    for u in room.users.exclude(id=kwargs['instance'].author.id):
        group = str(u)
        response = Response(data=kwargs['json'], status=status.HTTP_201_CREATED)
        async_to_sync(layer.group_send)(group, {'type': callback,
                                                'response': make_response(response, callback)})

# def open_room(layer, callback, **kwargs):
#     room = kwargs['instance']
#     for u in room.users.exclude(id=room.author.id):
#         group = str(u)
#         response = Response(data=kwargs['json'], status=status.HTTP_201_CREATED)
#         async_to_sync(layer.group_send)(group, {'type': callback,
#                                                'response': make_response(response, callback)})



