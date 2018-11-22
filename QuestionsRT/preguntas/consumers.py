from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from .models import Pregunta


# @ClassroomVirtual: permite la implementacion de websockets dentro de Django

class ClassroomVirtual(WebsocketConsumer):


# @def coonect: metodo que crea un canal de difusion para los mensajes
# y poder conectarse en este caso llamado "chat"

    def connect(self):
        async_to_sync(self.channel_layer.group_add)("chat", self.channel_name)
        self.accept()

# @def_receive: metodo que recibe el id de la pregunta, donde esta se busca en la base de datos y
# es enviada en un Json llamado 'Data' al grupo de difusion

    def receive(self, text_data):
        pregunta = Pregunta.objects.get(pk=text_data)

        data = {
                'pregunta': str(pregunta.pregunta),
                'falso': str('Falso'),
                'verdadero': str('Verdadero'),
                'id_pregunta': int(pregunta.id),
                'tipo': str('Pregunta de Falso o Verdadero')
            }


        async_to_sync(self.channel_layer.group_send)(
            "chat",
            {
                'type': 'chat_message',
                'message': data
            }
        )

# @def chat_message: metodo que recoge el Json Data y lo envia de nuevo a la pagina web,
# para que este sea visualizado a todos los usuarios que estan dentro de la Url

    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps(message))

# @def disconnect: metodo que permite desconectarse del websocket

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)("chat", self.channel_name)
