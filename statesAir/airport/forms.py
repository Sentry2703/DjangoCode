from django import forms

from .models import Plane, Flight, Department, Employee, Crew

class DepartmentForm(forms.Form):
    dept_id = forms.IntegerField()
    dept_name = forms.ChoiceField(choices=Department.DepartmentName.choices, required=True)
    dept_location = forms.CharField(max_length=50)

class CreateDepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['dept_id', 'dept_name', 'dept_location']
