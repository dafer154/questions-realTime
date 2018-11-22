from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from .models import Pregunta

class ClassroomVirtual(WebsocketConsumer):

    def connect(self):
        async_to_sync(self.channel_layer.group_add)("chat", self.channel_name)
        self.accept()

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

    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps(message))


    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)("chat", self.channel_name)
