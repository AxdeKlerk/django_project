from django.shortcuts import render
from django.http import HttpResponse    #importing the HttpResponse class from the django.http module

# Create your views here.
def index(request):
    # This function handles the request and returns a response
    # The request parameter is an HttpRequest object that contains metadata about the request
    if request.method == "GET":
        return HttpResponse("You have GETed something")
    elif request.method =="POST":
        return HttpResponse("You have POSTed something")
    else:
        return HttpResponse("Hello Ax!")  #returning a simple HTTP response with the text "Hello Ax!"