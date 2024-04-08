from django.urls import  path
from . import consumers


ASGI_urlpatters = [
    path('websocket/<int:id>',consumers.ChatConsumer.as_asgi()),
]