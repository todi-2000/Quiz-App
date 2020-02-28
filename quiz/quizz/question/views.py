from django.shortcuts import render,get_object_or_404
from .models import Question,Choice
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,"question/home.html")

def rules(request):
    return render(request,'question/rules.html')

@login_required
def details(request,question_id):
    question=Question.objects.get(pk=question_id)
    choice=Choice.objects.get(question=question.id)
    if request.method=='POST':
        if request.POST.get('ans',default=None) == choice:
            messages.success(request,f'Correct Answer')
            print('correct')
    context={
        'question':question
    }

    return render(request,'question/details.html',context)
