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


application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter([
            # URLRouter just takes standard Django path() or url() entries.
            path("classroom/stream", ClassroomVirtual),
        ]),
    ),

})

# application = ProtocolTypeRouter({
#     path("classroom/stream", ClassroomVirtual),
# })