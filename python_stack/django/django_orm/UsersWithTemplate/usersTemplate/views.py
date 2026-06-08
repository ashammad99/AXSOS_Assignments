from django.shortcuts import render, redirect

from usersTemplate.models import User


# Create your views here.
def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})


def add_user(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        age = request.POST['age']

        User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            age=age
        )
        return redirect('user_list')