from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('rules/',views.rules,name='rules'),
    path('questions/<int:level>/',views.details,name='detail'),
    path('leaderboard/',views.leaderboard,name='leaderboard'),
]
