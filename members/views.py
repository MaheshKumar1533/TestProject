from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from members.models import userDetails
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse
from django.contrib.auth.models import User



def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

# def signup(request):
#     template = loader.get_template('signup.html')
#     return HttpResponse(template.render())

def custom_login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    User = authenticate(request,username=username,password=password)
    print(User)
    if User is not None:
        login(request,User)
        return render(request, 'dashboard.html')
    else:
        return render(request,"custom_login.html")
        
    

@login_required
def dashboard(request):
    template = loader.get_template('dashboard.html')
    return HttpResponse(template.render())

def signup(request):
    if request.method == 'POST':
        name = request.POST.get("username")
        email = request.POST.get("email")
        number = int(request.POST.get("number"))
        password = request.POST.get("password")
        record = userDetails()
        record.name=name
        record.email = email
        record.number = number    
        record.password = password
        record.save()
        return render(request, "custom_login.html")
    return render(request, "signup.html")