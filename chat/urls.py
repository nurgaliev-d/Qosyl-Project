from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MessageViewSet

router = DefaultRouter()
router.register(r'messages', MessageViewSet)

urlpatterns = router.urls

    
urlpatterns += [
    # path('chat/<str:room_name>/', views.chat_room, name='chat_room'),
    path('chat/<int:user_id>/', views.chat_room, name='chat_room'),
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),
]