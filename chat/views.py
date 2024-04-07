from django.shortcuts import render
from django.views import View


class Main(View):
    def get(self,request):
        # request.session['get_me_from_the_consumer']='this is me'
        # print(request.session.get('get_me_from_the_main_page'))# None, because you can only edit session from view not from consumers
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