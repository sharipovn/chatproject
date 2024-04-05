from django.urls import  path
from . import consumers


ASGI_urlpatters = [
    path('websocket/',consumers.ChatConsumer.as_asgi()),
]