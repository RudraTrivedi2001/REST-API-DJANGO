from django.urls import path 
from .views import get_users, create_User, user_details

urlpatterns = [
    path('users/', get_users, name='get_users'),
    path('user/', create_User, name= 'create_User'),
    path('user/<int:pk>/', user_details, name='user_details'),
]