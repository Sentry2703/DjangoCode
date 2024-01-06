from django import forms

from .models import Plane, Flight, Department, Employee, Crew

class CreateDepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"

class CreateEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        widgets = {
            'emp_date': forms.DateInput(attrs={'type': 'date'})
        }

class EditEmployeeForm(forms.Form):
    employee = forms.ModelChoiceField(queryset=Employee.objects.all())

class CreatePlaneForm(forms.ModelForm):
    class Meta:
        model = Plane
        fields = "__all__"
        widgets = {
            'commission_date': forms.DateInput(attrs={'type': 'date'})
        }

class EditPlaneForm(forms.Form):
    plane = forms.ModelChoiceField(queryset=Plane.objects.all())
    
class CreateFlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = "__all__"
        widgets = {
            'flight_departure': forms.DateInput(attrs={'type': 'date'}),
            'flight_arrival': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super(CreateFlightForm, self).__init__(*args, **kwargs)
        self.fields['flight_plane'].queryset = Plane.objects.filter(plane_status='Active')