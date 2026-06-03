import random
from datetime import datetime
from django.shortcuts import render, redirect


def index(request):
    # Initialize session values if they don't exist
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    return render(request, 'index.html')


def process_money(request):
    if request.method == 'POST':
        building = request.POST.get('building', '')

        gold = 0
        if building == 'farm':
            gold = random.randint(10, 20)
        elif building == 'cave':
            gold = random.randint(5, 10)
        elif building == 'house':
            gold = random.randint(2, 5)
        elif building == 'casino':
            gold = random.randint(-50, 50)

        # Update session gold
        request.session['gold'] = request.session.get('gold', 0) + gold

        # Build activity message
        time = datetime.now().strftime("%Y/%m/%d %I:%M %p")
        if gold >= 0:
            message = f"Earned {gold} gold from the {building}! ({time})"
        else:
            message = f"Entered a casino and lost {abs(gold)} gold... Ouch. ({time})"

        # Prepend to activities list (newest first)
        activities = request.session.get('activities', [])
        activities.insert(0, message)
        request.session['activities'] = activities

    return redirect('index')
