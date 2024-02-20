from django.db import models
from django.contrib.auth.models import User

# Create your models here.'


class Topic(models.Model):
    name= models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Room(models.Model):
    host= models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    topic= models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=200)
    description= models.TextField(null=True,blank=True)#null true means it can be left blank
    #participants=
    updated= models.DateTimeField(auto_now=True) #captures instance every single time  a room is updated  and therefore model is updated
    created= models.DateTimeField(auto_now_add=True) #captures instances once a room is created and thats it
    
    def __str__(self):
        return self.name # this represents the models in string format rather than just object models in the database
    
    
class Message(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    room= models.ForeignKey(Room,on_delete=models.CASCADE) #iif a room gets deleted all the children of it gets deleted
    body= models.TextField()
    updated= models.DateTimeField(auto_now=True) 
    created= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.body[0:50] # [0:50] limits the preview message so that it wont be cluttered