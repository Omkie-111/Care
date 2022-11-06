from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# after addd on
from base.models import BaseModel
from django.utils.text import slugify

# Create your models here.

class Department(models.Model):
    choose=[('1','Dermatology'),('2','Neurology'),('3','Cardiology'),('4','Orthology'),('5','Gynaecology'),('6','Nephrology'),('7','Gastrology'),('8','Urology'),('9','Onchology'),]
    Department_Img = models.ImageField()
    #slug = models.SlugField(unique = True, null = True, blank = True) # used to slugify the urls
    Department_Name = models.CharField(max_length=200,choices=choose,default=" ")


    def __str__(self):
        return self.Department_Name

    def __unicode__(self):
        return u'%s' % (self.Department_Name)

class Member(models.Model):
    Image = models.ImageField(upload_to = 'pics')
    Name = models.CharField(max_length =150)
    Specialisation = models.CharField(max_length=200,default='')
    Department = models.ForeignKey(Department,on_delete=models.CASCADE)
    Education = models.TextField()

    def __str__(self):
        return self.Name 

    def __unicode__(self):
        return u'%s' % (self.Name)

    def department_name(self):
        return self.Department.Department_Name
       

class Appointment(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200,default="")
    email = models.EmailField( max_length=200,default="")
    phone = models.PositiveBigIntegerField()
    datetime = models.DateTimeField(blank=True, null=True,default=timezone.now)
    depart = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    doctor = models.ForeignKey(Member, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.first_name

    def __init__(self, *args, **kwargs):
        super(Appointment,self).__init__(*args, **kwargs)
        self.fields['doctor'].queryset = Member.objects.none()

        if 'depart' in self.data:
            try:
                depart_id = int(self.data.get('depart'))
                self.fields['doctor'].queryset = Member.objects.filter(depart_id=depart_id).order_by('Name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty doctor queryset
        elif self.instance.pk:
            self.fields['doctor'].queryset = self.instance.depart.doctor_set.order_by('Name')


class Contact(models.Model):
    name = models.CharField(max_length = 200,default="")
    email = models.EmailField(max_length = 150)
    subject = models.CharField(max_length = 300,default="")
    phone = models.CharField(max_length=11)
    message = models.CharField(max_length = 2000)

    def __str__(self):
        return self.name
"""
class Attendance(BaseModel):
    # Member Attendance
    id = models.AutoField(primary_key=True)
    mark_attendance = models.BooleanField(default=False)
    attendance_date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        
        return str(self.attendance_date)
"""