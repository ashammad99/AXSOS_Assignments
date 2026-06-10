from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render, redirect
from .models import Dojo, Ninja

def index(request):
    dojos = Dojo.objects.all()
    context = {
        'dojos': dojos
    }
    return render(request, 'index.html', context)

def create_dojo(request):
    if request.method == 'POST':
        name = request.POST['name']
        city = request.POST['city']
        state = request.POST['state']
        Dojo.objects.create(name=name, city=city, state=state)
    return redirect('/')

def create_ninja(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dojo_id = request.POST['dojo']
        dojo = Dojo.objects.get(id=dojo_id)
        Ninja.objects.create(first_name=first_name, last_name=last_name, dojo=dojo)
    return redirect('/')

# NINJA BONUS
def delete_dojo(request, dojo_id):
    dojo = Dojo.objects.get(id=dojo_id)
    dojo.delete()
    return redirect('/')