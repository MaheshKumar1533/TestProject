from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from members.models import userDetails

def members(request):
    template = loader.get_template('signup.html')
    return HttpResponse(template.render())

def submit(request):
    name = request.GET["username"]
    #email = request.GET["email"]
    number = int(request.GET["number"])
    password = request.GET["password"]
    record = userDetails()
    record.name=name
    #record.email = email
    record.number = number
    record.password = password
    record.save()
    template = loader.get_template("result.html")
    return HttpResponse(template.render())