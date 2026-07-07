from django.shortcuts import render
from django.http import HttpResponse
from .models import Milestone

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def milestones(request):
    return render(request, 'milestones/index.html', {'milestones': Milestone.objects.all()})

def milestone_detail(request, milestone_id):
    milestone = Milestone.objects.get(id=milestone_id)
    return render(request, 'milestones/detail.html', {'milestone': milestone})