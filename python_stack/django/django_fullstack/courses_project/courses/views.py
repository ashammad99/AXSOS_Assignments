from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Course, Comment, DescriptionModel


# READ - Index (All Courses)
def index(request):
    """Display form and all courses"""
    courses = Course.objects.all()
    context = {
        'courses': courses,
        'errors': {}
    }
    return render(request, 'courses/index.html', context)


# CREATE - Add Course
def add_course(request):
    """Process add course form"""
    if request.method == 'POST':
        data = {
            'name': request.POST.get('name', ''),
            'description': request.POST.get('description', ''),
        }

        result = Course.objects.create_course(data)

        if result['success']:
            course = result['course']
            messages.success(request, f'{course.name} added successfully!')
            return redirect('courses:index')
        else:
            courses = Course.objects.all()
            context = {
                'courses': courses,
                'errors': result['errors'],
                'old_data': data
            }
            return render(request, 'courses/index.html', context)

    return redirect('courses:index')


# DELETE - Confirmation Page
def delete_course_confirmation(request, course_id):
    """Show delete confirmation page"""
    course = get_object_or_404(Course, id=course_id)
    context = {'course': course}
    return render(request, 'courses/delete_confirmation.html', context)


# DELETE - Process Delete
def delete_course(request, course_id):
    """Delete course and redirect"""
    course = get_object_or_404(Course, id=course_id)
    course_name = course.name

    # Delete the course (description will cascade delete)
    course.delete()

    messages.success(request, f'{course_name} deleted successfully!')
    return redirect('courses:index')


# NINJA BONUS - Comments Page
def course_comments(request, course_id):
    """Show comments page for a course"""
    course = get_object_or_404(Course, id=course_id)
    comments = course.comments.all()

    context = {
        'course': course,
        'comments': comments,
        'errors': {}
    }
    return render(request, 'courses/comments.html', context)


# NINJA BONUS - Add Comment
def add_comment(request, course_id):
    """Add comment to course"""
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        comment_text = request.POST.get('comment', '').strip()

        if not comment_text:
            context = {
                'course': course,
                'comments': course.comments.all(),
                'errors': {'comment': 'Comment cannot be empty'}
            }
            return render(request, 'courses/comments.html', context)

        if len(comment_text) < 5:
            context = {
                'course': course,
                'comments': course.comments.all(),
                'errors': {'comment': 'Comment must be at least 5 characters'}
            }
            return render(request, 'courses/comments.html', context)

        Comment.objects.create(course=course, text=comment_text)
        messages.success(request, 'Comment added successfully!')
        return redirect('courses:course_comments', course_id=course_id)

    return redirect('courses:course_comments', course_id=course_id)