from django.shortcuts import render
from django.http import HttpResponse
from .forms import DepartmentForm, CreateDepartmentForm
from .models import Employee, Department, Plane, Flight, Crew

def home(request):
    return render(request, 'airport/home.html')

def create_dep(request):
    form = CreateDepartmentForm()
    if request.method == "POST":
        form = CreateDepartmentForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form" : form}
    return render(request, 'airport/create_dep.html', context)

def list_things(request):
    emp = Employee.objects.all()
    content = {"emp" : emp}
    return render(request, 'airport/list_things.html', content)