# import json
# from channels import Group, Channel
# from .models import Pregunta
# from channels.auth import channel_session_user, channel_session_user_from_http
# from django.contrib.auth.models import User, Group, Permission
# #from usuarios.models import Us



from django.conf import settings
from channels.generic.websocket import AsyncJsonWebsocketConsumer
#from .exceptions import ClientError


# def ws_add(message):
#     message.reply_channel.send({"accept": True})
#     Group("classroom").add(message.reply_channel)
#
# @channel_session_user_from_http
# def ws_message(message):
#     print("prueba Real time")
#
#
# def ws_disconnect(message):
#     Group("classroom").discard(message.reply_channel)



class ClassroomVirtual(AsyncJsonWebsocketConsumer):
    """
    This chat consumer handles websocket connections for chat clients.
    It uses AsyncJsonWebsocketConsumer, which means all the handling functions
    must be async functions, and any sync work (like ORM access) has to be
    behind database_sync_to_async or sync_to_async. For more, read
    http://channels.readthedocs.io/en/latest/topics/consumers.html
    """

    ##### WebSocket event handlers

    async def connect(self):

        await self.accept()

    async def receive_json(self, content):
        """
        Called when we get a text frame. Channels will JSON-decode the payload
        for us and pass it as the first argument.
        """
        # Messages will have a "command" key we can switch on
        command = content.get("command", None)
        try:
            if command == "join":
                # Make them join the room
                await self.join_room(content["room"])
            elif command == "leave":
                # Leave the room
                await self.leave_room(content["room"])
            elif command == "send":
                await self.send_room(content["room"], content["message"])
        except ClientError as e:
            # Catch any errors and send it back
            await self.send_json({"error": e.code})

    async def disconnect(self, code):
        """
        Called when the WebSocket closes for any reason.
        """
        # Leave all the rooms we are still in
        for room_id in list(self.rooms):
            try:
                await self.leave_room(room_id)
            except ClientError:
                pass


    async def chat_message(self, event):
        """
        Called when someone has messaged our chat.
        """
        # Send a message down to the client
        await self.send_json(
            {
                "msg_type": settings.MSG_TYPE_MESSAGE,
                "room": event["room_id"],
                "username": event["username"],
                "message": event["message"],
            },
        )
