from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    
    def connect(self):
        self.accept()

        self.send('{"type": "accept","status":"accepted"}')

    
    def receive(self,text_data):
        print(text_data)



    def disconnect(self,code):
        print(code)
        #operations
        print("Hello! the connection is disconnected or stopped")