
from django.urls import re_path
# from . import consumers
from chat import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<user_id>\d+)/$', consumers.ChatConsumer.as_asgi()),
]
