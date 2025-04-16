from django.urls import path

from .views import log, register, logout_user

# app_name = 'users'  # при подключении namespace

urlpatterns = [
    path('log/', log, name='log'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout_user')
]
