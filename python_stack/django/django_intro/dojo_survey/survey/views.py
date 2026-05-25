from django.shortcuts import render, redirect

def index(request):
    return render(request, 'survey/index.html')

def result(request):
    if request.method == 'POST':
        print("POST data:", request.POST)
        context = {
            'name': request.POST.get('name', ''),
            'dojo_location': request.POST.get('dojo_location', ''),
            'favorite_language': request.POST.get('favorite_language', ''),
            'experience': request.POST.get('experience', ''),
            'interests': request.POST.getlist('interests'),
            'comment': request.POST.get('comment', ''),
        }
        return render(request, 'survey/result.html', context)
    return redirect('/')
