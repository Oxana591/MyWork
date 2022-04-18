from django.http import HttpResponse
from django.shortcuts import render
import datetime



def index(request):
    return render(request,"site1/index.html") 

def func1(request):
    now = datetime.datetime.now()
    html="<html><body><h1>Зараз: %s.<h1></body></html>" %now
    return HttpResponse(html)

def hi(request,name):
    return HttpResponse(f"Привіт,<span style=\"color:yellow;text-shadow:2px -2px 5px blue;font-size:22pt\"> {name.capitalize()}</span>!")