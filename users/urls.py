from django.urls import path
from . import views

# app_name = 'users'

urlpatterns = [
    # path('login/', views.loginPage, name="login"),
    path('login/',views.loginPage, name = "login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    path('update-user/', views.updateUser, name="update-user"),
    path('topics/', views.topicsPage, name="topics"),
    path('all/', views.get_all_users, name='all_users'),
    path('friends/', views.friends_view, name='friends'),
    path('profile/<str:username>/', views.userProfile, name='profile'),
    path('add_friend/<str:username>/', views.add_friend_view, name='add_friend'),
    path('profile/<int:user_id>/', views.userProfile, name='profile'),
    path('send-friend-request/<int:user_id>/', views.send_friend_request, name='send_friend_request'),
    path('remove-friend/<int:user_id>/', views.remove_friend, name='remove_friend'),
    path('analytics/', views.analytics, name='analytics'),
]