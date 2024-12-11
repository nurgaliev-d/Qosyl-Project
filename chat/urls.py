from django.urls import path
from . import views

urlpatterns = [
    # path('chat/<str:room_name>/', views.chat_room, name='chat_room'),
    path('chat/<int:user_id>/', views.chat_room, name='chat_room'),
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),
]