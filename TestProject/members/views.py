from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from members.models import userDetails

def members(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def submit(request):
    number = int(request.GET["username"])
    password = request.GET["password"]
    record = userDetails()
    record.number = number
    record.password = password
    record.save()
    template = loader.get_template("result.html")
    return HttpResponse(template.render())