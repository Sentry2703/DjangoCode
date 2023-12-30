from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the indx of Demo Project.")

def home(request):
    return HttpResponse("Welcome to the Little Lemon Website")
# Create your views here.
