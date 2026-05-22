from django.shortcuts import render, redirect
from time import strftime,localtime
import requests

def root(request):
    return redirect('index') 

def index(request):

    try:
        response = requests.get(
        "https://timeapi.io/api/Time/current/zone?timeZone=Asia/Gaza"
        )

        data = response.json()

        timeInternet = data['dateTime']

    except Exception as e:
        timeInternet = f"Error: {e}"
    
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", localtime()),
        "internet_time": timeInternet
    }
    return render(request,'index.html', context=context)