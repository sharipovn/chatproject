from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from .models import Message
from django.contrib.auth.models import User
from datetime  import datetime


class ChatConsumer(WebsocketConsumer):
    
    def connect(self):
        self.accept()
        
        
        self.person_id = self.scope.get("url_route").get('kwargs').get('id')        
    
    
    def receive(self,text_data):
        text_data=json.loads(text_data)
        print(text_data.get('type'))
        print(text_data.get('message'))
        
        
        new_message = Message()
        new_message.from_who = self.scope.get("user")
        new_message.to_who = User.objects.get(id=self.person_id)
        new_message.message = text_data.get('message')
        new_message.date =  datetime.now().date()
        new_message.time =  datetime.now().time()
        new_message.has_been_seen= False
        new_message.save()
        
        
    def receiver_function(self,the_data_will_come_from_layer):
        print(the_data_will_come_from_layer)