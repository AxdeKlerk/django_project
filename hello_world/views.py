from django.shortcuts import render
from django.http import HttpResponse    #importing the HttpResponse class from the django.http module

# Create your views here.
def index(request):
    if request.method =="POST":
        return HttpResponse("You have POSTed something")
    else:
        return HttpResponse(request) #returning the request object as a response