from django.conf import settings
from django.shortcuts import render, redirect, HttpResponse
from care.settings import EMAIL_HOST_USER
from .forms import AppointmentForm
from .models import Appointment, Department,Member, Contact
from django.contrib import messages
from django.template import Context
from django.core.mail import EmailMessage
from django.template.loader import get_template
import json as simplejson


# Create your views here.
def home(request):
    #context = {'variable':"Hi,you are welcomed between 10 A.M. to 12 A.M."}
    return render(request,'nindex.html')
    #return HttpResponse("Welcome to the Homepage!")

def about(request):
    return render(request,'about.html')

def facilities(request):
    return render(request,'facilities.html')

def team(request):
    data = Member.objects.all
    context={'data':data}
    return render(request,"index.html",context)


def appoint(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        dateTime = request.POST.get("dateTime")
        phone = request.POST.get("phone")
        depart = request.POST.get("depart")
        doctor = request.POST.get("doctor")

        dateTime = dateTime.split()
        Depart = Department.objects.get(id=depart)
        Doctor = Member.objects.get(id=doctor)

        appoint = Appointment.objects.create(first_name=first_name,last_name=last_name,email=email,date=dateTime[0],time=dateTime[1],phone=phone,depart=Depart,doctor=Doctor)
        appoint.save()
        
        data = {
        'name':appoint.first_name,
        'email':appoint.email,
        'date':appoint.date,
        'time':appoint.time,
        'phone':appoint.phone,
        'depart':appoint.depart,
        'doctor':appoint.doctor,
        }


        message = get_template('email.html').render(data)
        mail = EmailMessage(
            "About your appointment",
            message,
            EMAIL_HOST_USER,
            [email],
            reply_to=[EMAIL_HOST_USER]
        )
        mail.content_subtype = "html"
        mail.send()
        messages.success(request, "Your appointment has been booked successfully. Thank you!")
        #return redirect("/")

    else:
        return render(request,"index.html")



def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        phone = request.POST["phone"]
        message = request.POST["message"]


        #if request.method == "POST":
        contact = Contact(name=name,email=email,subject=subject,phone=phone,message=message)
        contact.save()
        messages.success(request, "Your request has been sent successfully. Thank you!")
        return redirect("/")

    else:
        return render(request,"index.html")

# For implementing python in javascript

def get_details(request):
    depart_id = request.GET.get('depart_id')
    doctors = Member.objects.filter(Department_id=depart_id).all()
    return render(request, 'doctor_dropdown_list_options.html', {'doctors': doctors})






    
        

