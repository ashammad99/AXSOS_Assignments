from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='users_register'),
    path('login', views.login, name='users_login'),
    path('users/new', views.register, name='users_new'),
    path('users', views.index, name='users_index'),
]
