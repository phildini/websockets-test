from channels.generic.websocket import JsonWebsocketConsumer
from asgiref.sync import async_to_sync


class NotificationConsumer(JsonWebsocketConsumer):
    def connect(self):
        user = self.scope["user"]
        async_to_sync(self.channel_layer.group_add)("hello", "hello")
        self.accept()
        async_to_sync(self.channel_layer.group_send)(
            "hello", {"type": "chat.message", "content": "hello"}
        )

    def receive_json(self, content, **kwargs):
        print(content)
        async_to_sync(self.channel_layer.group_send)(
            "hello", {"type": "chat.message", "content": "hello"}
        )
        print("Here we are")

    def chat_message(self, event):
        self.send_json(content=event["content"])

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)("hello", "hello")
