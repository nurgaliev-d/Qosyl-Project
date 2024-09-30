from django.urls import path
from .views import organization_list

urlpatterns = [
    path('organizations/', organization_list, name='organization-list'),
]
