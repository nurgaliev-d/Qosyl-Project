from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rooms.models import Room 
from chat.models import Message
from users.models import  Topic 
from django.http import HttpResponse
from rooms.forms import  RoomForm
from django.http import JsonResponse
from django.db.models import Count
from rest_framework import viewsets
from .serializers import RoomSerializer
import logging

def room(request, pk):
    try:
        room = Room.objects.get(id=pk)
    except Room.DoesNotExist:
        logger.error("Room with id %s does not exist", pk)
        return HttpResponse('Room not found', status=404)

    logger.info("Room %s accessed by user: %s", room.name, request.user)
    
    room_messages = room.message_set.all()
    participants = room.participants.all()

    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room', pk=room.id)

    context = {'room': room, 'room_messages': room_messages,
               'participants': participants}
    return render(request, 'rooms/room.html', context)

logger = logging.getLogger(__name__)

@login_required(login_url='login')
def createRoom(request):
    logger.info("Create Room view accessed by user: %s", request.user)
    form = RoomForm()
    topics = Topic.objects.all()
    if request.method == 'POST':
        logger.debug("Form submitted with data: %s", request.POST)
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
        )
        logger.info("Room created successfully by user: %s", request.user)
        return redirect('home')

    context = {'form': form, 'topics': topics}
    return render(request, 'rooms/room_form.html', context)



@login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    topics = Topic.objects.all()
    if request.user != room.host:
        return HttpResponse('Your are not allowed here!!')

    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get('description')
        room.save()
        return redirect('home')

    context = {'form': form, 'topics': topics, 'room': room}
    return render(request, 'rooms/room_form.html', context)


@login_required(login_url='login')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse('Your are not allowed here!!')

    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'rooms/delete.html', {'obj': room})

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
