from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('contact',views.contact, name="Contact"),
    path('appoint',views.appoint,name="Appointment"),
    path('get_details/', views.get_details, name='get_doctor_details'),
]