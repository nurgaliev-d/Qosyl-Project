from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout

from users.models import User, MyChats
from .models import  Message


# Create your views here.

# rooms = [
#     {'id': 1, 'name': 'Lets learn python!'},
#     {'id': 2, 'name': 'Design with me'},
#     {'id': 3, 'name': 'Frontend developers'},
# ]


@login_required(login_url='login')
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse('Your are not allowed here!!')


    if request.method == 'POST':
        message.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': message})

@login_required
def index(request):
    frnd_name = request.GET.get('user', None)
    mychats_data = None
    if frnd_name:
        if User.objects.filter(username=frnd_name).exists() and MyChats.objects.filter(me=request.user,
                                                                                       frnd=User.objects.get(
                                                                                               username=frnd_name)):
            frnd_ = User.objects.get(username=frnd_name)
            mychats_data = MyChats.objects.get(me=request.user, frnd=frnd_)
    frnds = User.objects.exclude(id=request.user.id)
    return render(request, 'chat/index.html', {'my': mychats_data, 'chats': mychats_data, 'frnds': frnds})