from django.shortcuts import render
from django.views import View
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync



class Main(View):
    def get(self,request):
        
        data={
            "type": "receiver.function",
            "message":"hi Nuriddin this event from the views"
        }
        channel_layer=get_channel_layer()
        async_to_sync(channel_layer.group_send)("test",data)
        
        return render(request=request,template_name='chat/main.html')
    
    
class Login(View):
    def get(self,request):
        return render(request=request,template_name='chat/login.html')
    
    

class Register(View):
    def get(self,request):
        return render(request=request,template_name='chat/register.html')

    
    
class Logout(View):
    def get(self,request):
        #run operations
        pass



    
    
class Home(View):
    def get(self,request):
        return render(request=request,template_name='chat/home.html')
    

class ChatPerson(View):
    def get(self,request):
        return render(request=request,template_name='chat/chat_person.html')