import random
from django.shortcuts import render, redirect


def index(request):
    # Reset only if no game in progress
    if 'number' not in request.session:
        request.session['number'] = random.randint(1, 100)
        request.session['attempts'] = 0
        request.session['result'] = None
        request.session['game_over'] = False

    return render(request, 'index.html', {
        'result': request.session.get('result'),
        'attempts': request.session.get('attempts'),
        'number': request.session.get('number'),
        'game_over': request.session.get('game_over'),
    })
def reset(request):
    request.session.flush()
    return redirect('index')
def guess(request):
    if request.method != 'POST':
        return redirect('index')

    if request.session.get('game_over'):
        request.session.flush()
        return redirect('index')

    user_guess = int(request.POST['guess'])
    number = request.session['number']

    request.session['attempts'] += 1

    if request.session['attempts'] >= 5 and user_guess != number:
        request.session['result'] = 'lose'
        request.session['game_over'] = True
        return redirect('index')

    if user_guess > number:
        request.session['result'] = 'high'
    elif user_guess < number:
        request.session['result'] = 'low'
    else:
        request.session['result'] = 'correct'
        request.session['game_over'] = True

    # Mark session as modified since we mutated a nested value
    request.session.modified = True

    return redirect('index')
