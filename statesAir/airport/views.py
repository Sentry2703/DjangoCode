from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateDepartmentForm, CreateEmployeeForm, CreateFlightForm, CreatePlaneForm
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

def create_emp(request):
    form = CreateEmployeeForm()
    if request.method == "POST":
        form = CreateEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form" : form}
    return render(request, 'airport/create_emp.html', context)

def create_plane(request):
    form = CreatePlaneForm()
    if request.method == "POST":
        form = CreatePlaneForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form" : form}
    return render(request, 'airport/create_plane.html', context)

def create_flight(request):
    form = CreateFlightForm()
    if request.method == "POST":
        form = CreateFlightForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form" : form}
    return render(request, 'airport/create_flight.html', context)

def list_deps(request):
    deps = Department.objects.all()
    content = {"deps" : deps}
    return render(request, 'airport/list_deps.html', content)

def list_emps(request):
    emps = Employee.objects.all()
    content = {"emps" : emps}
    return render(request, 'airport/list_emps.html', content)

def list_planes(request):
    planes = Plane.objects.all()
    content = {"planes" : planes}
    return render(request, 'airport/list_planes.html', content)

def list_flights(request):
    flights = Flight.objects.all()
    content = {"flights" : flights}
    return render(request, 'airport/list_flights.html', content)