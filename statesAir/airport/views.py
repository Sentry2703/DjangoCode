from django.shortcuts import render
from django.http import HttpResponse
from .forms import DepartmentForm, CreateDepartmentForm

def home(request):
    return HttpResponse("This is the Airport Application")

def form(request):
    form = DepartmentForm()
    context = {"form" : form}
    return render(request, 'airport/form.html', context)

def create_dep(request):
    form = CreateDepartmentForm()
    if request.method == "POST":
        form = CreateDepartmentForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form" : form}
    return render(request, 'airport/create_dep.html', context)