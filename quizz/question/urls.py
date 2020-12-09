from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('rules/',views.rules,name='rules'),
    path('questions/',views.details,name='detail'),
    path('leaderboard/',views.leaderboard,name='leaderboard'),
    path("end/<int:score>", views.end, name="end"),
    path("like", views.like, name="like"),
    path("status", views.status, name="status")
]
