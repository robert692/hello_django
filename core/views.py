from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(requests, name):
    return HttpResponse(f"Hello {name}")