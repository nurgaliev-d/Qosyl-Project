from django.urls import path
from .views import *

urlpatterns = [
    path('organizations/', organization_list, name='organization-list'),
    path('products/', product_list, name='product-list'),
    path('user-profiles/', user_profile_list, name='user-profile-list'),
    path('profile/', current_user_profile, name='current-user-profile'),
    path('profile/<int:user_id>/', other_user_profile, name='other-user-profile'),
    path('publications/', publication_list, name='publication-list'),
    path('publications/create/', create_publication, name='create-publication'),
    path('publications/<int:pk>/', get_publication, name='get-publication'),
    path('publications/<int:pk>/update/', update_publication, name='update-publication'),
    path('publications/<int:pk>/delete/', delete_publication, name='delete-publication'),
    path('publications/<int:pk>/like/', like_publication, name='like-publication'),
]

