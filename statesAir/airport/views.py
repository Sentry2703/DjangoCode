from django.shortcuts import render
from django.http import HttpResponse
from django import forms
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

def edit_crew(request):
    crew = None
    select = EditCrewForm()
    selectEmp = EditEmployeeForm()
    selectEmp.fields['employee'].queryset = Employee.objects.filter(emp_role__dept_name='Pilot') | Employee.objects.filter(emp_role__dept_name='FlightAttendant')
    selectEmp2 = EditEmployeeForm()

    if request.method == "GET":
        if 'crew' in request.GET:
            crew = Crew.objects.get(pk = int(request.GET.get('crew')))
            select = EditCrewForm(initial={'crew': crew})
            selectEmp.fields['employee'].queryset = Employee.objects.filter(emp_role__dept_name='Pilot') | Employee.objects.filter(emp_role__dept_name='FlightAttendant')
            selectEmp.fields['employee'].queryset = selectEmp.fields['employee'].queryset.exclude(emp_id__in=crew.crew_staff.all())
            selectEmp2.fields['employee'].queryset = crew.crew_staff.all()
        
    elif request.method == "POST":
        if 'type' in request.POST:
            crew = Crew.objects.get(pk=request.GET.get('crew'))
            if request.POST.get('type') == "add":
                print("Added: "+ request.POST.get('employee'))
                crew.crew_staff.add(Employee.objects.get(pk=request.POST.get('employee')))
            else:
                print("Removed: "+ request.POST.get('employee'))
                crew.crew_staff.remove(Employee.objects.get(pk=request.POST.get('employee')))
            crew.save()

    return render(request, 'airport/edit_crew.html', {"select": select, "selectEmp": selectEmp, "selectEmp2": selectEmp2})