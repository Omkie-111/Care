from django.core.checks import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def register(request):

    if request.method =="POST":

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.info(request,"Username already exists")
            return redirect('Register')

        elif User.objects.filter(email=email).exists():
            messages.info(request,"Email exists")
            return redirect('Register')

        else:
            user =User.objects.create_user(username=username, password=password, email=email, first_name=first_name,last_name=last_name)
            user.save()
            print("User created")
            return redirect('Login')

    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')



