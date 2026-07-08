from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Milestone
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class Home(LoginView):
    template_name = 'home.html'

class MilestoneCreate(LoginRequiredMixin, CreateView):
    model = Milestone
    fields = ['title', 'date', 'category', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class MilestoneUpdate(LoginRequiredMixin, UpdateView):
    model = Milestone
    fields = ['title', 'date', 'category', 'description']

class MilestoneDelete(LoginRequiredMixin, DeleteView):
    model = Milestone
    success_url = '/milestones/'

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

@login_required
def milestone_index(request):
    milestones = request.user.milestones.all()
    return render(request, 'milestones/index.html', {'milestones': milestones})

@login_required
def milestone_detail(request, milestone_id):
    milestone = Milestone.objects.get(id=milestone_id)
    return render(request, 'milestones/detail.html', {'milestone': milestone})