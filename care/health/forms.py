from django import forms
from .models import Member ,Appointment

# Create your forms here.

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['doctor'].queryset = Member.objects.none()

            if 'depart' in self.data:
                try:
                    depart_id = int(self.data.get('depart'))
                    self.fields['doctor'].queryset = Member.objects.filter(depart_id=depart_id).order_by('Name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty doctor queryset
            elif self.instance.pk:
                self.fields['doctor'].queryset = self.instance.depart.doctor_set.order_by('Name')

