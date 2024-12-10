from django.urls import path
from . import views

urlpatterns = [
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),
    path('chat/', views.index, name="chat")
]