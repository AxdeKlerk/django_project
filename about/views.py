from django.shortcuts import render
from django.http import HttpResponse   # importing the HttpResponse class from the django.http module

# Create your views here.
def about_me(request):
    return HttpResponse("This would be the about page")  # returning a simple HTTP response with the text "This would be the about page"