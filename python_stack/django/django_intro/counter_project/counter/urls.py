from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('increment/<int:amount>/', views.increment_by, name='increment_by'),
    path('custom_increment/', views.custom_increment, name='custom_increment'),
    path('destroy_session/', views.destroy_session, name='destroy_session'),
]
