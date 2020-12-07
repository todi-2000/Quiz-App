from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse, Http404

a = False
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

def details(request):
    if request.user.is_authenticated:
        st=Student.objects.get(student=request.user)
        level=st.slevel
        try:
            quest=Question.objects.get(level=level)
            choice=str(Choice.objects.get(question=quest.id))
            context = {'ques':quest, "auth": request.user.is_authenticated, "like_count": len(quest.likes.all()), "liked": quest in st.liked.all()}
            if request.method=='POST':
                if request.POST.get("expired") == "YES":
                    level += 1
                    st.slevel=level
                    st.save()
                    try:
                        nextques= Question.objects.get(level=level)
                        context={'ques':nextques}
                        return JsonResponse({'ques': nextques.question_text})
                    except Question.DoesNotExist:
                        return JsonResponse({'ques': 'done'})
                else:
                    c=request.POST['ans']
                    if c.lower() == choice.lower(): #correct
                        st.score+=quest.max_marks
                        level += 1
                        st.slevel=level
                        st.save()
                        try:
                            nextques= Question.objects.get(level=level)
                            return JsonResponse({'ques': nextques.question_text})
                        except Question.DoesNotExist:
                            global a
                            a = True
                            return JsonResponse({'ques': "done", "score": st.score})
                    return JsonResponse({'ques': 'wrong'})
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

def end(request, score):
    global a
    if not a:
        raise Http404("Wrong Requst")
    else:
        a = False
        return render(request, "question/quiz-end-page.html", {"score": score})

def like(request):
    if request.method == "POST" and request.user.is_authenticated:
        st=Student.objects.get(student=request.user)
        level=st.slevel
        quest=Question.objects.get(level=level)
        print(quest.question_text);
        if request.POST.get("update_like") == "YES":
            liked = quest in st.liked.all()
            if liked:
                st.liked.remove(quest)
            else:
                st.liked.add(quest)
            st.save()
        return JsonResponse({"like_count": len(quest.likes.all()), "liked": quest in st.liked.all()})
    raise Http404("Wrong Request")