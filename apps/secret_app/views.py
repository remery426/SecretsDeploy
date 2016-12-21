from django.shortcuts import render, redirect
from ..login_app.models import User
from .models import Secret_Post
from django.contrib import messages
import calendar
import datetime
# Create your views here.
def index(request):
    if request.session['thisuser'] == '':
        return redirect('/')
    current_user = User.objects.get(email=request.session['thisemail'])
    all_posts = Secret_Post.objects.all()
    likes = Secret_Post.objects.filter(likes=current_user)

    context = {
        "secrets" : all_posts,
        "liked" : likes,
        "now" :datetime.datetime.now()
        }
    return render(request, 'secret_app/index.html', context)
def createpost(request):

    current_user = User.objects.get(email=request.session['thisemail'])
    response = Secret_Post.objects.makePost(request.POST, current_user)
    if not response['status']:
        for error in response['error']:
            messages.error(request, error)

    return redirect('secret_app/dashboard')
def logout(request):
    request.session['thisuser'] = ''
    return redirect('/')
def delete(request, id):
    this_secret =Secret_Post.objects.get(id=id)
    this_secret.delete()
    return redirect('secret_app/dashboard')
def like(request, id):
    this_secret =Secret_Post.objects.get(id=id)
    current_user = User.objects.get(email=request.session['thisemail'])
    this_secret.likes.add(current_user)
    return redirect('secret_app/dashboard')
