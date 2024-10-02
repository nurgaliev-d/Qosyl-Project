from django.urls import path
from .views import *

urlpatterns = [
    path('organizations/', organization_list, name='organization-list'),
    path('products/', product_list, name='product-list'),
    path('user-profiles/', user_profile_list, name='user-profile-list'),
    path('profile/', current_user_profile, name='current-user-profile'),
    path('profile/<int:user_id>/', other_user_profile, name='other-user-profile')
]
