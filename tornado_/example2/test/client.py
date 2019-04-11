from tornado.websocket import websocket_connect
from tornado.ioloop import IOLoop

import json

msg = {
    'id': 1,
    'method':  'POST',
    'url': '/auth/registration',
   'args': {
       'token': 'aGFicmFoYWJyX2FkbWlu'
        },
   'body': {
       'username': 'habrahabr',
       'password': 'mysupersecretpassword',
   },
}




async def test():
    client = await websocket_connect('ws://localhost:8000')
    await client.write_message(json.dumps(msg))


IOLoop.current().run_sync(test)