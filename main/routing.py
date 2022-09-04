from email.mime import application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from chat_seller import routing
import chat_seller
application=ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(
        URLRouter(
            chat_seller.routing.websocket_url_patterns
        )
    ),
})