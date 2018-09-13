from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json


class ClassroomVirtual(WebsocketConsumer):

    def connect(self):
        print("hablame conectadooooooo")

    def disconnect(self, close_code):
        print("chao papaaaaa")

    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)

    def send_message(self, message):
        self.send(text_data=json.dumps(message))
