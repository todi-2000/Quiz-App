from django.urls import path
from . import views


urlpatterns = [
    path('questions/',views.QuestionsView.as_view(),name='questions'),
    path('students/',views.StudentsView.as_view(),name='students'),
    path('choices/',views.ChoicesView.as_view(),name='choices'),

    path('questions/<pk>',views.QuestionView.as_view(),name='questions'),
    path('students/<pk>',views.StudentView.as_view(),name='students'),
    path('choices/<pk>',views.ChoiceView.as_view(),name='choices'),
]
