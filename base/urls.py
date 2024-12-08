
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('activity/', views.activityPage, name="activity"),
    path('room/<int:pk>/delete/', views.room_delete, name='room_delete')
]

