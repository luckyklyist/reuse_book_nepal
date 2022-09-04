from django.urls import re_path
from . import consumer

websocket_url_patterns=[
    re_path(r'ws/chat/(?P<room_name>\w+,)$',consumer.ChatRoomConsumer),
]