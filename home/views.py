from typing import Reversible
from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.urls import reverse

from home.forms import CreateUserForm,ProfileForm
# Create your views here.

# views.py
from .forms import AvatarUploadForm

def index(request):
    user = request.user

    if request.method == 'POST':
        form = AvatarUploadForm(request.POST, request.FILES, instance=user.profile)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the same page or wherever you want

    else:
        form = AvatarUploadForm(instance=user.profile)

    return render(request, 'index.html', {'user': user, 'form': form})


def loginuser(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        user= authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.info(request,f"Welcome, @{username} your are successfully logged in")
            return redirect('home') 
        else:
            messages.info(request,"Invalid username or password")


            return redirect('login')
    return render(request,'login.html')

@login_required(login_url='login')

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        request.session.flush()
        messages.info(request,"Succesfully logged out")
        return redirect('login')
    
def registeruser(request):
    form= CreateUserForm()
    if request.method=='POST':
         
         
         form= CreateUserForm(request.POST)
         if form.is_valid():
                   form.save()
                   messages.info(request,' New profile created, click on login')
                   redirect('login')
         else:
             context={'form':form}
             messages.info(request,'Invalid credential')
             return render(request,'register.html',context)
    
    
    context={'form':form}
    return render(request,'register.html',context)

@login_required(login_url='login')
def profile(request):
     
     
     if request.method=='POST':
          form= ProfileForm(request.POST,request.FILES,instance=request.user.profile)
          if form.is_valid():
                   username=request.user.username
                   form.save()
                   
                   messages.success(request,f'@{username}, your profile has been updated')
                   print("kndknk")
                   return redirect('home')
                   
     else:
          form=ProfileForm(instance=request.user.profile)
     context={'form':form}
     
     return render(request,'profile.html',context)
    
     