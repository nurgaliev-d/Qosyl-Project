# C:\Users\Lenovo\Desktop\Qosyl-Project\chat\views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import  Message

from rest_framework import viewsets
from .serializers import MessageSerializer

from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseForbidden

User = get_user_model()

def chat_room(request, user_id):
    recipient = get_object_or_404(User, id=user_id)  # Используем user_id для поиска пользователя
    return render(request, 'chat/chat_room.html', {
        'recipient': recipient,
    })

@login_required(login_url='login')
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)

    if request.user != message.sender:
        return HttpResponseForbidden('You are not allowed to delete this message!')


    if request.method == 'POST':
        message.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': message})

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
