from django.shortcuts import render
from .models import Room

# Create your views here.

rooms=[ 
       {'id':1,'name':'Lets learn django'},
       {'id':2,'name':'Lets make some projects'},
       {'id':3,'name':'front end developemnt?'}
    
]

def home (request):
    rooms= Room.objects.all()
    context= {'rooms':rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = None
    for i in rooms:
        if i ['id']==int(pk):
            room=i
        context = {'room': room}
    return render(request, 'base/room.html',context)
