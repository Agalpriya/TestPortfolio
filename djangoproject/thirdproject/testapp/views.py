from django.shortcuts import render
from django.http import HttpResponse

def one(request):
    return HttpResponse('<h1> i am one </h1>')


def two(request):
    return HttpResponse('<h1> i am two </h1>')

# Create your views here.
