from django.urls import path
from . import views


urlpatterns = [
    # Home
    path('', views.home, name='home'),
    
    # Book URLs
    path('books/', views.book_list, name='book_list'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('books/<int:book_id>/edit/', views.book_update, name='book_update'),
    path('books/<int:book_id>/delete/', views.book_delete, name='book_delete'),
    path('books/<int:book_id>/remove-author/<int:author_id>/', views.book_remove_author, name='book_remove_author'),
    
    # Author URLs
    path('authors/', views.author_list, name='author_list'),
    path('authors/<int:author_id>/', views.author_detail, name='author_detail'),
    path('authors/<int:author_id>/edit/', views.author_update, name='author_update'),
    path('authors/<int:author_id>/delete/', views.author_delete, name='author_delete'),
    path('authors/<int:author_id>/remove-book/<int:book_id>/', views.author_remove_book, name='author_remove_book'),
]
