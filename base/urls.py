from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home,name='Homepage'),
    path('room/',views.room,name='RoomPage'),
]


