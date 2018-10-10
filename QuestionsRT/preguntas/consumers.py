from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from .models import Pregunta


class ClassroomVirtual(WebsocketConsumer):

    def connect(self):
        print("hablame conectadooooooo")



    def receive(self, text_data):

        pregunta = Pregunta.object.get(pk=(text_data['text']))

        Group("chat").send({

            'text': json.dumps({
                'pregunta': str(pregunta.pregunta),
                'falso': str('Falso'),
                'verdadero': str('Verdadero'),
                'id_pregunta': int(pregunta.id),
                'tipo': str('Pregunta de Falso o Verdadero'),
            })
        })

        print(pregunta)

        data = json.loads(text_data)
        self.commands[data['command']](self, data)

    #
    # def disconnect(self, close_code):
    #     print("chao papaaaaa")

    def send_message(self, message):
        self.send(text_data=json.dumps(message))
