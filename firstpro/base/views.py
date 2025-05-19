from django.shortcuts import render
from django.http import HttpResponse

rooms = [
    {'id': 1, 'name': 'Room 1'},
    {'id': 2, 'name': 'Room 2'},
    {'id': 3, 'name': 'Room 3'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'home.html', context)
def room(request):
    room = None
    for i in rooms:
        if i['id'] == int(request.GET.get('id')):
            room = i
    context = {'room': room}
    return render(request, 'room.html', context)