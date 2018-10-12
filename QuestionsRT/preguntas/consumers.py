from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from .models import Pregunta


class ClassroomVirtual(WebsocketConsumer):

    def connect(self):
        # Called on connection.
        # To accept the connection call:
        self.accept()
        # Or accept the connection and specify a chosen subprotocol.
        # A list of subprotocols specified by the connecting client
        # will be available in self.scope['subprotocols']




    def receive(self, text_data):

        pregunta = Pregunta.objects.get(pk=text_data)

        print(pregunta);

        data = {
            'pregunta': str(pregunta.pregunta),
            'falso': str('Falso'),
            'verdadero': str('Verdadero'),
            'id_pregunta': int(pregunta.id),
            'tipo': str('Pregunta de Falso o Verdadero')
        }

        prueba = json.dumps(data);
        print(prueba);

        self.send(text_data=json.dumps(data))

        #self.send({'text': json.dumps(data)})


    def send_message(self, message):
        self.send(text_data=json.dumps(message))
