from django.db import models

# Create your models here.
class Room(models.Model):
    #hoat=
    #topic=
    name=models.CharField(max_length=200)
    description= models.TextField(null=True,blank=True)#null true means it can be left blank
    #participants=
    updated= models.DateTimeField(auto_now=True) #captures instance every single time  a room is updated  and therefore model is updated
    created= models.DateTimeField(auto_now_add=True) #captures instances once a room is created and thats it
    
    def __str__(self):
        return self.name
        