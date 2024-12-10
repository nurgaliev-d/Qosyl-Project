import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import async_to_sync
from users.models import MyChats, User
from channels.db import  database_sync_to_async
import datetime
class ChatApp(AsyncJsonWebsocketConsumer):
    async def connect(self):
        print("connecting...")
        await self.accept()
        await self.channel_layer.group_add(f"mychat_app{self.scope['user']}" ,self.channel_name)

    async def receive(self, text_data):
        text_data = json.loads(text_data)
        await self.channel_layer.group_send(
            f"mychat_app{text_data['user']}",
            {
                "type":"send.msg",
                "msg" : text_data['msg']
            }
        )
        await self.save_chat(text_data)
    @database_sync_to_async
    def save_chat(self,text_data):
        frnd = User.objects.get(username=text_data['user'])
        mychats, created = MyChats.objects.get_or_create(me=self.scope['user'], frnd=frnd)
        if created:
            mychats.chats = {}
        mychats.chats[str(datetime.datetime.now()) + '1'] = {'user': 'me', 'msg': text_data['msg']}
        mychats.save()
        mychats, created = MyChats.objects.get_or_create(me=frnd, frnd=self.scope['user'])
        if created:
            mychats.chats = {}
        mychats.chats[str(datetime.datetime.now())+'1'] = {'user':frnd.username,'msg':text_data['msg']}
        mychats.save()
    async def send_msg(self,event):
        print(event)
        await self.send(event['msg'])
    async def disconnect(self, close_code):
        pass
