from django.shortcuts import render
from django.http import HttpResponse
def wish(HttpRequest):
    message='<h1> Hi , I am Agal<h1>'
    return HttpResponse(message)
# Create your views here.
