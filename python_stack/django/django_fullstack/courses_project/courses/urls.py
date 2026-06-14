from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    # Index
    path('', views.index, name='index'),

    # Create
    path('add/', views.add_course, name='add_course'),

    # Delete
    path('delete/<int:course_id>/', views.delete_course_confirmation, name='delete_confirmation'),
    path('destroy/<int:course_id>/', views.delete_course, name='delete_course'),

    # NINJA BONUS - Comments
    path('comments/<int:course_id>/', views.course_comments, name='course_comments'),
    path('comments/<int:course_id>/add/', views.add_comment, name='add_comment'),
]