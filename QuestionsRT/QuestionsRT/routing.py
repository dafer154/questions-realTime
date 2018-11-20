from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from preguntas.consumers import ClassroomVirtual


websocket_urlpatterns = [
    path("classroom/stream", ClassroomVirtual),
]

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        ),
    ),

})
