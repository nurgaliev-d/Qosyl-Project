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
]