from django.shortcuts import render
from django.http import HttpResponse    #importing the HttpResponse class from the django.http module

# Create your views here.
def index(request):
    return HttpResponse("Hello, World!")  #returning a simple HTTP response with the text "Hello, World!"