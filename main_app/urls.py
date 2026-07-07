from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('milestones/', views.milestones, name='milestones'),
    path('milestones/<int:milestone_id>/', views.milestone_detail, name='milestone_detail')
]
