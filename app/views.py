from django.shortcuts import render,redirect
from django.http import HttpResponse
##from django.contrib.auth.models import User,auth
from .models import user
from django.contrib import messages
#from django.contrib.auth.decorators import login_required 
# Create your views here.

#@login_required
def home(request):
    return render(request, 'home.html',{'name':'welcome'})

def Register(request):
    if request.method=='POST':
        user_name=request.POST['username']
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        email_name=request.POST['email']
        age=request.POST['age']
        password1=request.POST['password']
        password2=request.POST['password1']
        address=request.POST["address"]
        
        if(password1==password2):
            if user.objects.filter(username=user_name).exists():
                messages.info(request,'username taken')
                ##print('user name taken')
                return redirect('Register')
            elif user.objects.filter(email=email_name):
                messages.info(request,'email taken')
                #print('email already taken')
            else:
                User=user.objects.create(username=user_name,fistname=first_name,lastname=last_name,email=email_name,age=age,password=password1,address=address)
                User.save();
                messages.info(request,'user created')
                print("user created")
                return render(request,'login.html',{'name':user_name})
        else:
           ## print('password not matching')
            messages.info(request,'password not matching')
            return redirect('Register')
    else:
        return render(request,'register.html',{})
    
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        #user=auth.authenticate(username=username,password=password)
        
        if user.objects.filter(username=username).exists():
            if user.objects.filter(password=password).exists():
                #if user is not None:
                    #auth.login(request.user)
                return render(request, 'home.html',{'name':username})
            else:
                messages.info(request,'invalid')
                return redirect('login')
        else:
            messages.info(request,'invalid')
            return redirect('login')

    else:    
        return render(request,'login.html')

def logout(request):
    return render(request,'login.html')