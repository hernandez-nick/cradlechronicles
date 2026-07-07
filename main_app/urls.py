from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('milestones/', views.milestones, name='milestones'),
    path('milestones/<int:milestone_id>/', views.milestone_detail, name='milestone_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),

]
