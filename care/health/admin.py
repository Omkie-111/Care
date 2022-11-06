from django.contrib import admin
from django.db import models
from .models import Member,Department,Appointment,Contact
from django.utils.html import format_html

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
            return format_html('<img src="{}" width="150" height="150"/>'.format(obj.Image.url))

    image_tag.short_description = 'Image'

    list_display=['id','image_tag','Name','Specialisation','Department','Education']
    filter = ['Name']

admin.site.register(Member,MemberAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
            return format_html('<img src="{}" width="150" height="150"/>'.format(obj.Department_Img.url))

    image_tag.short_description = 'Image'

    list_display=['id','image_tag','Department_Name']
    filter = ['Department_Name']

admin.site.register(Department,DepartmentAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','email','datetime','depart','doctor']
    filter = ('first_name','last_name','datetime','doctor')

admin.site.register(Appointment,AppointmentAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display=['name','email','subject','phone','message']
    filter = ['name','phone','email']

admin.site.register(Contact,ContactAdmin)

#class AttendanceAdmin(admin.ModelAdmin):
 #   list_display = ['attendance_date','mark_attendance']
    
#admin.site.register(Attendance,AttendanceAdmin)
#admin.site.register(AttendanceReport)

#class Doctor(admin.ModelAdmin):
   # list_display = ['department','doctor']

#admin.site.register(Doctor)