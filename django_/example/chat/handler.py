from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import sync_to_async
import json

from chat.apps.core.utils import parse_msg, get_endpoint, make_request, make_response
from chat.apps.myauth.utils import get_user
from inspect import iscoroutinefunction

from rest_framework import status
from django.utils import timezone

class WSHandler(AsyncJsonWebsocketConsumer):


    async def connect(self):
        print(self.scope['path'], 'path!!!')
        await self.accept()

    async def _send(self, response):
        if status.is_client_error(response['status_code']) or status.is_server_error(response['status_code']):
            print(response)
        print(json.dumps(response))
        await self.send_json(response)


    def set_channel_group(self, request):
        user = get_user(request)
        print(user, '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! USER', request)
        request.channel_group = str(user)
        request.channel_name = self.channel_name
        if user.is_authenticated:
            user.last_seen = timezone.now()
            user.save(update_fields=['last_seen'])

    # async def handle_exceptions(self, exc, id):
    #     error = {'name': type(exc).__name__, 'msg': str(exc)}
    #     await self._send({'error': error, 'id': id,  'status_code': 400})

    async def receive_json(self, msg, **kwargs):
        id, method, url, params, body, headers = parse_msg(msg)
        print(msg)
        # try:
        endpoint, args, kwargs = get_endpoint(url)
        print(endpoint)

        request = make_request(self.scope, url, method, params, body, headers)

        self.set_channel_group(request)

        if iscoroutinefunction(endpoint):
            response = await endpoint(request, *args, **kwargs)
        else:
            response = await sync_to_async(endpoint)(request, *args, **kwargs)
        response = make_response(response, id)
        self.last_request = request
        await self._send(response)


        # except Exception as exc:
        #     await self.handle_exceptions(exc, id)


    async def disconnect(self, close_code):
        try:
            await self.channel_layer.group_discard(self.last_request.channel_group, self.channel_name)
        except Exception:
            pass


    async def send_message(self, event):
        response = event['response']
        print('SEND', response)
        await self._send(response)

    #
    # async def open_room(self, event):
    #     response = event['response']
    #     print('SEND', response)
    #     await self._send(response)




{
   'method': 'POST',
   'url': '/users/create',
   'params': {
       'token': 'aGFicmFoYWJyX2FkbWlu'
   },
   'data': {
       'username': 'habrahabr',
       'password': 'mysupersecretpassword',
   },
    'id': 1,
}

"""
Main page

"""