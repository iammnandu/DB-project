from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("HOME")
def about(request):
    return HttpResponse("ABOUT")
def booking(request):
    return HttpResponse("BOOK")
def doctors(request):
    return HttpResponse("DOCTORS")
def contact(request):
    return HttpResponse("CONTACT")

