from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.http import JsonResponse
import json


def index(request):
    """Display login/registration page"""
    if 'user_id' in request.session:
        return redirect('success')
    return render(request, 'login_reg.html')


def register(request):
    """Handle user registration"""
    if request.method == 'POST':
        data = {
            'first_name': request.POST.get('first_name', ''),
            'last_name': request.POST.get('last_name', ''),
            'email': request.POST.get('email', ''),
            'password': request.POST.get('password', ''),
            'confirm_pw': request.POST.get('confirm_pw', ''),
            'birthday': request.POST.get('birthday', ''),
        }

        result = User.objects.create_user(data)

        if result['success']:
            user = result['user']
            request.session['user_id'] = user.id
            request.session['user_name'] = user.get_full_name()
            messages.success(request, f'Successfully registered!')
            return redirect('success')
        else:
            for field, error in result['errors'].items():
                messages.error(request, error)
            return render(request, 'login_reg.html', {
                'old_data': data,
                'errors': result['errors']
            })

    return redirect('index')


def login(request):
    """Handle user login"""
    if request.method == 'POST':
        data = {
            'email': request.POST.get('email', ''),
            'password': request.POST.get('password', '')
        }

        errors = User.objects.login_validator(data)

        if errors:
            for field, error in errors.items():
                messages.error(request, error)
            return render(request, 'login_reg.html', {
                'login_errors': errors,
                'login_data': data
            })

        user = User.objects.get(email=data['email'])
        request.session['user_id'] = user.id
        request.session['user_name'] = user.get_full_name()
        messages.success(request, f'Successfully logged in!')
        return redirect('success')

    return redirect('index')


def success(request):
    """Display success page (session protected)"""
    if 'user_id' not in request.session:
        messages.error(request, 'You must be logged in to view this page')
        return redirect('index')

    try:
        user = User.objects.get(id=request.session['user_id'])
    except User.DoesNotExist:
        request.session.flush()
        return redirect('index')

    context = {
        'user': user,
        'user_name': request.session.get('user_name', '')
    }
    return render(request, 'success.html', context)


def logout(request):
    """Handle user logout"""
    request.session.flush()
    messages.success(request, 'Successfully logged out!')
    return redirect('index')


def check_email_ajax(request):
    """Check if email is unique via AJAX"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email', '').strip().lower()

            if not email:
                return JsonResponse({'available': False, 'message': 'Email is required'})

            if User.objects.filter(email=email).exists():
                return JsonResponse({'available': False, 'message': 'Email already in use'})
            else:
                return JsonResponse({'available': True, 'message': 'Email is available'})
        except:
            return JsonResponse({'error': 'Invalid request'})

    return JsonResponse({'error': 'Method not allowed'})