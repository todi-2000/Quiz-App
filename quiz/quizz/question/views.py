from django.shortcuts import render,get_object_or_404
from .models import Question,Choice
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request,"question/home.html")

def rules(request):
    return render(request,'question/rules.html')

@login_required
def details(request,question_id):
    quest=Question.objects.get(pk=question_id)
    choice=str(Choice.objects.get(question=quest.id))
    context = {'ques':quest}
    if request.method=='POST':
        c=request.POST['ans'] 
        if c==choice:
            question_id += 1
            nextques= Question.objects.get(pk=question_id)
            context={'ques':nextques}
            return HttpResponseRedirect("/questions/"+str(question_id))
    return render(request,'question/details.html',context)
