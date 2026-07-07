from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Milestone
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

class Home(LoginView):
    template_name = 'home.html'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('milestone-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    return render(request, 'signup.html', {'form': form, 'error_message': error_message})

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def milestones(request):
    return render(request, 'milestones/index.html', {'milestones': Milestone.objects.all()})

def milestone_detail(request, milestone_id):
    milestone = Milestone.objects.get(id=milestone_id)
    return render(request, 'milestones/detail.html', {'milestone': milestone})