from tornado.websocket import websocket_connect
import json



data = {
   'method': 'POST',
   'url': '/test/test_set/0/add_user/',
   'params': {
       'token': 'aGFicmFoYWJyX2FkbWlu'
   },
   'data': {
       'username': 'Borisov',
       'password': '19960213Z26a',
   },
    'id':'2'
}



async def test():
    con = await websocket_connect('ws://localhost:8000')
    await con.write_message(json.dumps(data))
    print(await con.read_message())


import asyncio

asyncio.get_event_loop().run_until_complete(test())


