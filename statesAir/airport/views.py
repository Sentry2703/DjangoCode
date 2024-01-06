from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
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

def list_crews(request):
    crews = Crew.objects.all().prefetch_related('crew_staff')
    content = {"crews" : crews}
    return render(request, 'airport/list_crews.html', content)

def edit_emp(request):
    emp = None
    select = EditEmployeeForm()
    edit = CreateEmployeeForm()

    if request.method == "GET":
        if 'employee' in request.GET:
            emp = Employee.objects.get(pk = int(request.GET.get('employee')))
            select = EditEmployeeForm(initial={'employee': emp})
            edit = CreateEmployeeForm(instance=emp)
        
    elif request.method == "POST": 
        emp = Employee.objects.get(pk=request.GET.get('employee'))
        edit = CreateEmployeeForm(request.POST, instance=emp)
        if edit.is_valid():
            edit.save()
    
    return render(request, 'airport/edit_emp.html', {"select": select, "form" : edit})

def edit_plane(request):
    plane = None
    select = EditPlaneForm()
    edit = CreatePlaneForm()

    if request.method == "GET":
        if 'plane' in request.GET:
            plane = Plane.objects.get(pk = int(request.GET.get('plane')))
            select = EditPlaneForm(initial={'plane': plane})
            edit = CreatePlaneForm(instance=plane)
        
    elif request.method == "POST": 
        plane = Plane.objects.get(pk=request.GET.get('plane'))
        edit = CreatePlaneForm(request.POST, instance=plane)
        if edit.is_valid():
            edit.save()
    
    return render(request, 'airport/edit_plane.html', {"select": select, "form" : edit})