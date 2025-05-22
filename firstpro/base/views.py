from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

# rooms = [
#     {'id': 1, 'name': 'Room 1'},
#     {'id': 2, 'name': 'Room 2'},
#     {'id': 3, 'name': 'Room 3'},
# ]

def main(request):
    return render(request, 'main.html')
def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'home.html', context)
def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'room.html', context)
def room_form(request):
    context = {}
    return render(request, 'room_form.html', context)