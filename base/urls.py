from django.urls import path, include
from . import views  
from rest_framework.routers import DefaultRouter
from .views import BaseViewSet

router = DefaultRouter()
router.register(r'base', BaseViewSet)

urlpatterns = router.urls


urlpatterns = [
    path('', views.home, name="home"),
    path('activity/', views.activityPage, name="activity"),
]
