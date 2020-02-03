from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages


# Create your views here.
def register(request):
    form=UserRegisterForm(request.POST)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Your account is successfully registered!!')
            return redirect('login')
        else:
            form=UserRegisterForm()
    return render(request,'users/register.html',{'form':form})



