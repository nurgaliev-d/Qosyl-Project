from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .models import  User , Topic, FriendRequest
from rooms.models import Room
from .forms import  UserForm, MyUserCreationForm
from django.http import JsonResponse
from django.db import connection
from django.db.models import Count
from django.core.serializers import serialize
from rooms.models import Room
from chat.models import Message
import json

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exit')

    context = {'page': page}
    return render(request, 'users/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'users/login_register.html', {'form': form})

def userProfile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    topics = Topic.objects.all()
    profile_user = get_object_or_404(User, id=pk)
    
    # Check if this is the logged-in user's profile
    is_own_profile = request.user == profile_user
    
    # Check if they are already friends
    is_friend = profile_user.is_friend(request.user)
    
    # Check if a friend request has already been sent
    existing_request = FriendRequest.objects.filter(from_user=request.user, to_user=profile_user).exists()

    context = {
        "user": profile_user,
        "is_own_profile": is_own_profile,
        "is_friend": is_friend,
        "existing_request": existing_request,
        'user': user, 
        'rooms': rooms,
        'room_messages': room_messages, 
        'topics': topics,
    }
    return render(request, "users/profile.html", context)



@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)

    return render(request, 'users/update-user.html', {'form': form})

def topicsPage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Topic.objects.filter(name__icontains=q)
    return render(request, 'users/topics.html', {'topics': topics})

@login_required
def get_all_users(request):
    users = User.objects.all()
    for user in users:
        user.avatar_url = user.avatar.url if user.avatar else '/static/images/default-avatar.jpg'
    return render(request, 'users/all_users.html', {'users': users})

def get_user_avatar(user):
    if user.avatar:
        return user.avatar.url
    else:
        return '/static/images/default-avatar.jpg'
    
@login_required
def send_friend_request(request, user_id):
    to_user = get_object_or_404(User, id=user_id)
    if request.user != to_user and not request.user.is_friend(to_user):
        FriendRequest.objects.create(from_user=request.user, to_user=to_user)
    return redirect("profile", user_id=user_id)

@login_required
def remove_friend(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.user.is_friend(user):
        request.user.remove_friend(user)
    return redirect("profile", user_id=user_id)

@login_required
def friends_view(request):
    user = request.user
    friends = user.friends.all()  # Assuming the friends relation is set up in the model
    return render(request, 'users/friends.html', {'friends': friends})

def profile_view(request, username):
    print(f"Fetching profile for username: {username}")
    profile_user = get_object_or_404(User, username=username)
    is_friend = profile_user in request.user.friends.all()
    return render(request, 'users/profile.html', {
        'user': profile_user,
        'is_friend': is_friend,
    })
    
@login_required
def add_friend_view(request, username):
    profile_user = get_object_or_404(User, username=username)
    if profile_user != request.user and profile_user not in request.user.friends.all():
        request.user.friends.add(profile_user)
        messages.success(request, f"You are now friends with {profile_user.username}!")
    else:
        messages.warning(request, "You are already friends or cannot add this user.")
    return redirect('profile', username=username)


def analytics(request):
    # Get the current user
    user = request.user
    
    # Annotate rooms with the count of comments made by the current user
    rooms = Room.objects.annotate(
        num_comments=Count('comments', filter=Q(comments__user=user), distinct=True)
    )

    # Prepare data for charts
    room_names = [room.name for room in rooms]
    num_comments = [room.num_comments for room in rooms]

    # Pass data to the template
    context = {
        'user': user,
        'is_own_profile': user == request.user,
        'room_names': json.dumps(room_names),  # Serialize as JSON
        'num_comments': json.dumps(num_comments),  # Serialize as JSON
    }

    return render(request, 'profile.html', context)