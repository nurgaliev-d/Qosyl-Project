# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from .models import Message1

User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Получаем user_id из URL
        self.recipient_id = self.scope['url_route']['kwargs']['user_id']
        self.sender = self.scope['user']

        # Проверка получателя по user_id
        self.recipient = await self.get_user_by_id(self.recipient_id)
        if not self.recipient:
            await self.close()
            return
        
        # Создание имени комнаты с использованием user.id
        self.room_name = f"chat_{min(self.sender.id, self.recipient.id)}_{max(self.sender.id, self.recipient.id)}"
        self.room_group_name = f"chat_{self.room_name}"

        # Добавляем пользователя в группу чата
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
    @database_sync_to_async
    def save_message(self, message):
            # Сохраняем сообщение в базе данных
        Message1.objects.create(sender=self.sender, recipient=self.recipient, content=message)
    async def disconnect(self, close_code):
        # Отключаем пользователя от группы чата
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Получаем сообщение из данных
        data = json.loads(text_data)
        message = data['message']
        
        # Сохранение сообщения в базе данных
        await self.save_message(message)

        # Отправка сообщения всем участникам группы
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )


    async def chat_message(self, event):
        # Отправка полученного сообщения пользователю
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))

    @database_sync_to_async
    def get_user_by_id(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None

   
    # @staticmethod
    # async def save_message(sender, recipient, content):
    #     from asgiref.sync import sync_to_async  # Импорт внутри функции для избежания конфликтов
    #     await sync_to_async(Message1.objects.create)(
    #         sender=sender,
    #         recipient=recipient,
    #         content=content
    #     )

