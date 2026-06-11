from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Book, Author
from django.db.models import Q

# ==================== HOME VIEW ====================

def home(request):
    """Redirect to book list"""
    return redirect('book_list')


# ==================== BOOK VIEWS ====================

def book_list(request):
    """Display all books and form to add a new book"""
    books = Book.objects.all()
    
    if request.method == 'POST':
        title = request.POST.get('title')
        
        if title:
            Book.objects.create(title=title)
            return redirect('book_list')
    
    context = {
        'books': books,
    }
    return render(request, 'books/book_list.html', context)


def book_detail(request, book_id):
    """Display a specific book and its authors"""
    book = get_object_or_404(Book, pk=book_id)
    authors = book.authors.all()
    
    # Get authors not yet associated with this book (for dropdown)
    available_authors = Author.objects.exclude(id__in=authors.values_list('id', flat=True))
    
    if request.method == 'POST':
        author_id = request.POST.get('author_id')
        if author_id:
            author = get_object_or_404(Author, pk=author_id)
            book.authors.add(author)
            return redirect('book_detail', book_id=book_id)
    
    context = {
        'book': book,
        'authors': authors,
        'available_authors': available_authors,
    }
    return render(request, 'books/book_detail.html', context)


def book_update(request, book_id):
    """Update a book"""
    book = get_object_or_404(Book, pk=book_id)
    
    if request.method == 'POST':
        book.title = request.POST.get('title', book.title)
        book.save()
        return redirect('book_detail', book_id=book_id)
    
    context = {'book': book}
    return render(request, 'books/book_update.html', context)


@require_http_methods(["POST"])
def book_delete(request, book_id):
    """Delete a book"""
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect('book_list')


@require_http_methods(["POST"])
def book_remove_author(request, book_id, author_id):
    """Remove an author from a book"""
    book = get_object_or_404(Book, pk=book_id)
    author = get_object_or_404(Author, pk=author_id)
    book.authors.remove(author)
    return redirect('book_detail', book_id=book_id)


# ==================== AUTHOR VIEWS ====================

def author_list(request):
    """Display all authors and form to add a new author"""
    authors = Author.objects.all()
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        notes = request.POST.get('notes')
        
        if first_name and last_name:
            Author.objects.create(
                first_name=first_name,
                last_name=last_name,
                notes=notes
            )
            return redirect('author_list')
    
    context = {
        'authors': authors,
    }
    return render(request, 'authors/author_list.html', context)


def author_detail(request, author_id):
    """Display a specific author and their books"""
    author = get_object_or_404(Author, pk=author_id)
    books = author.books.all()
    
    # Get books not yet associated with this author (for dropdown)
    available_books = Book.objects.exclude(id__in=books.values_list('id', flat=True))
    
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        if book_id:
            book = get_object_or_404(Book, pk=book_id)
            author.books.add(book)
            return redirect('author_detail', author_id=author_id)
    
    context = {
        'author': author,
        'books': books,
        'available_books': available_books,
    }
    return render(request, 'authors/author_detail.html', context)


def author_update(request, author_id):
    """Update an author"""
    author = get_object_or_404(Author, pk=author_id)
    
    if request.method == 'POST':
        author.first_name = request.POST.get('first_name', author.first_name)
        author.last_name = request.POST.get('last_name', author.last_name)
        author.notes = request.POST.get('notes', author.notes)
        author.save()
        return redirect('author_detail', author_id=author_id)
    
    context = {'author': author}
    return render(request, 'authors/author_update.html', context)


@require_http_methods(["POST"])
def author_delete(request, author_id):
    """Delete an author"""
    author = get_object_or_404(Author, pk=author_id)
    author.delete()
    return redirect('author_list')


@require_http_methods(["POST"])
def author_remove_book(request, author_id, book_id):
    """Remove a book from an author"""
    author = get_object_or_404(Author, pk=author_id)
    book = get_object_or_404(Book, pk=book_id)
    author.books.remove(book)
    return redirect('author_detail', author_id=author_id)
