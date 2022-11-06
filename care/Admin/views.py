from django.shortcuts import render,redirect
from health.models import Member, Department, Appointment

# Create your views here.

def member(request):
    data = Member.objects.all
    context={'data':data}
    return render(request,"member.html",context)

def index(request):
    return render(request,"admin/index.html")
