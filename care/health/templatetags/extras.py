from django.shortcuts import redirect
from django import template
from health.models import Member,Appointment,Department
from datetime import datetime

register = template.Library()

@register.simple_tag
def get_member():
    member = Member.objects.all
    return member

@register.simple_tag
def get_appointment():
    appoint = Appointment.objects.filter(datetime=datetime.date(datetime.today()))
    return appoint

@register.simple_tag
def get_department():
    depart = Department.objects.all
    return depart

@register.simple_tag
def get_site():
    return redirect("/")

@register.simple_tag
def get_doctor(value):
    doctors = Member.objects.filter(Department = value).distinct
    return {"doctors":doctors}

@register.inclusion_tag("appointment.html")
def get_doc(depart):
    choices = Member.objects.filter(Department = depart)
    return {"choices":choices}
