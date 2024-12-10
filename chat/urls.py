from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MessageViewSet

router = DefaultRouter()
router.register(r'messages', MessageViewSet)

urlpatterns = router.urls


urlpatterns += [
    
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),
    
]