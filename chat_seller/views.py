from multiprocessing import context
from django.shortcuts import render

def index(request):
    return render(request,"chat.html")

def room(request,room_name):
    context={'room_name':room_name}
    return render(request,"chat_room.html",context)

