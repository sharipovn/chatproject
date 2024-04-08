from django.db import models
from django.contrib.auth.models import User





class Message(models.Model):
    from_who = models.ForeignKey(User,on_delete=models.PROTECT,default=None,related_name='from_user')
    to_who= models.ForeignKey(User,on_delete=models.PROTECT,default=None,related_name='to_user')
    message = models.TextField()
    date= models.DateField(null=True)
    time=models.TimeField(null=True)
    has_been_seen= models.BooleanField(null=True,default=False)
    
    def __str__(self):
        return str(self.from_who)+" -> "+ str(self.to_who)
    
    

class UserChannel(models.Model):
    user=models.ForeignKey(User,on_delete=models.PROTECT,default=None)
    channel_name=models.TextField()
    
    
    def __str__(self):
        return str(self.user.username)+" - "+ str(self.channel_name)