"""
URL configuration for FirstDjanoProject project.
"""
from django.contrib import admin
from django.urls import path, include
from blogs import views as blogs_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # NINJA BONUS: root route uses the same method as /blogs
    path('', blogs_views.index, name='root'),

    path('blogs/', include('blogs.urls')),
    path('surveys/', include('surveys.urls')),
    path('', include('users.urls')),
]
