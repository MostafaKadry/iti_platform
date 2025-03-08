from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def create_member(request):
    return HttpResponse("Hello world!")

def retrive_member(request):
    return HttpResponse("Hello world!")

def delete_member(request):
    return HttpResponse("Hello world!")
def update_member(request):
    return HttpResponse("Hello world!")
