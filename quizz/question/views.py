from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        context={
            'user':request.user.username,
            'level':Student.objects.get(student=request.user).slevel-1,
            'score':Student.objects.get(student=request.user).score,
            'auth': request.user.is_authenticated
        }
        return render(request,"question/home.html",context)
    return render(request,"question/home.html")

def rules(request):
    return render(request,'question/rules.html', {"auth": request.user.is_authenticated})

def details(request,level):
    if request.user.is_authenticated:
        st=Student.objects.get(student=request.user)
        level=st.slevel
        try:
            quest=Question.objects.get(level=level)
            choice=str(Choice.objects.get(question=quest.id))
            context = {'ques':quest, "auth": request.user.is_authenticated}
            if request.method=='POST':
                c=request.POST['ans']
                if c.lower() == choice.lower():
                    st.score+=quest.max_marks
                    level += 1
                    st.slevel=level
                    st.save()
                    try:
                        nextques= Question.objects.get(level=level)
                        context={'ques':nextques}
                        return HttpResponseRedirect("/questions/"+str(level))
                    except Question.DoesNotExist:
                        return redirect("home")
                else:
                    return redirect("home")
            return render(request,'question/details.html',context)
        except Question.DoesNotExist:
                return redirect('home')
    else:
        return redirect('login')
 
def leaderboard(request):
    profiles = Student.objects.order_by('-score')
    context = {
        'profiles': profiles,
        "auth": request.user.is_authenticated
    }
    return render(request,'question/leaderboard.html',context=context)