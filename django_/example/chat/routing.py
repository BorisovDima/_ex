from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from .handler import WSHandler
from django.urls import path


application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([path('', WSHandler)])
    )
})

