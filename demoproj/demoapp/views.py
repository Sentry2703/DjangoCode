from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the index of Demo Project.")

def home(request):

    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info

    msg = """
            <h1>Welcome to the Little Lemon Website</h1>
            <br>
            <br>Path: {}
            <br>Scheme: {}
            <br>Method: {}
            <br>Address: {}
            <br>User Agent: {}
            <br>Path Info: {}""".format(path, scheme, method, address, user_agent, path_info)

    return HttpResponse(msg, content_type = "text/html", charset = "utf-8")

def form(request):
    return render(request, 'demoapp/form.html')

def form_submit(request):
    if request.method == "POST":
        username = request.POST.get('name')
        age = request.POST.get('age')
        return HttpResponse("Username: {}, Password: {}".format(username, age))
    else:
        return HttpResponse("Invalid request method.")