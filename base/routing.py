from django.urls import path
from base.consumers import ChatApp

websocket_urlpatterns = [
    path('ws/wsc/', ChatApp.as_asgi())
]
