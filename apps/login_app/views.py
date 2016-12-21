from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"login_app/index.html")
def success(request):
    return render(request,"login_app/success.html")
def register(request):

    response = User.objects.add_user(request.POST)
    if not response ['status']:
        for error in response['error']:
            messages.error(request, error)
        return redirect('/')
    context = {
        'current_user' : request.POST['first_name']
    }
    request.session['thisuser'] = ''
    for error in response['error']:
        messages.error(request, error)
    return redirect('/')
def login(request):
    response_1 = User.objects.login_user(request.POST)

    if not response_1['status']:
        for error in response_1['error']:
            messages.error(request, error)
        return redirect('/')
    request.session['thisuser']=response_1['user'][0].first_name
    request.session['thisemail']=response_1['user'][0].email
    print request.session['thisemail']
    return redirect('secret_app/dashboard')
