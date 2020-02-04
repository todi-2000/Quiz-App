from django.shortcuts import render
from .models import Question,Answer

# Create your views here.
def home(request):
    return render(request,"question/home.html")

def rules(request):
    return render(request,'question/rules.html')

def details(request,question_id):
    question=Question.objects.all()
    context={
        'question':question
    }
    return render(request,'question/details.html',context)
