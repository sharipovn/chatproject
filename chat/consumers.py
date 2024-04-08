from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync



class ChatConsumer(WebsocketConsumer):
    
    def connect(self):
        self.accept()
        self.send('{"type": "accept","status":"accepted"}')
        
        async_to_sync(self.channel_layer.group_add)('test',self.channel_name)

        
        
        
    
    def receive(self,text_data):
        print(text_data)
        self.send('{"type":"event_arrive","status":"arrived"}')


    def disconnect(self,code):
        print(code)
        #operations
        print("Hello! the connection is disconnected or stopped")
        
        
    def receiver_function(self,the_data_will_come_from_layer):
        print(the_data_will_come_from_layer)