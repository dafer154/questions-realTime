# from channels import include
#
# ASGI_APPLICATION = "QuestionsRT.routing.application"
#
#
# channel_routing = [
#     include("preguntas.routing.websocket_routing", path=r"^/classroom/stream"),
# ]


from django.urls import path
from channels.http import AsgiHandler
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

# application = ProtocolTypeRouter({
#     path("classroom/stream", ClassroomVirtual),
# })