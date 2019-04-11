from rest_framework.routers import DefaultRouter

from django.urls import path, include
from . import endpoints


router = DefaultRouter()
router.register('room', endpoints.RoomAPI, basename='room')
router.register('message', endpoints.MessageAPI, basename='message')


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/event_subscribe/', endpoints.EventGroupAPI.as_view()),
    path('', endpoints.Index.as_view())
]
