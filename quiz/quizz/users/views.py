from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib import messages,auth
from question.models import *


# Create your views here.
def register(request):
    form=UserRegisterForm(request.POST)
    if request.method=='POST':
        if form.is_valid():
            p=form.save()
            Student.objects.create(student=p)
            username=form.cleaned_data.get('username')
            messages.success(request,f'Your account is successfully registered!!')
            return redirect('login')
        else:
            form=UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

def login(request):
    form=UserLogInForm(request.POST)
    if request.method=='POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        print(request.POST['username'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'users/login.html')
    else:
        form=UserLogInForm()
    return render(request,'users/login.html',{'form':form})

def logout(request):
    auth.logout(request)
    return redirect('home')





