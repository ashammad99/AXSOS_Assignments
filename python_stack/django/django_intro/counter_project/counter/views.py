from django.shortcuts import render, redirect


def index(request):
    # Initialize session keys if they don't exist
    if 'visit_count' not in request.session:
        request.session['visit_count'] = 0
    if 'counter' not in request.session:
        request.session['counter'] = 0

    # Increment visit count every time this page is loaded
    request.session['visit_count'] += 1

    context = {
        'visit_count': request.session['visit_count'],
        'counter': request.session['counter'],
    }
    return render(request, 'counter/index.html', context)


def increment_by(request, amount):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    request.session['counter'] += amount
    return redirect('index')


def custom_increment(request):
    if request.method == 'POST':
        try:
            amount = int(request.POST.get('amount', 1))
        except ValueError:
            amount = 1
        if 'counter' not in request.session:
            request.session['counter'] = 0
        request.session['counter'] += amount
    return redirect('index')


def destroy_session(request):
    request.session.flush()
    return redirect('index')
