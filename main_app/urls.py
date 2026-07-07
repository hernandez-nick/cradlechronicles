from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('milestones/', views.milestone_index, name='milestone-index'),
    path('milestones/<int:milestone_id>/', views.milestone_detail, name='milestone-detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('milestones/create/', views.MilestoneCreate.as_view(), name='milestone-create'),

]
