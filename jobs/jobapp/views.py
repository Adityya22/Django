# from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def koljobs(request):
    s = 'Kolkata Jobs Information'
    return HttpResponse(s)


def mumjobs(request):
    s = 'Mumbai Jobs Information'
    return HttpResponse(s)


def bangjobs(request):
    s = 'Bangalore Jobs Information'
    return HttpResponse(s)


def punejobs(request):
    s = 'Pune Jobs Information'
    return HttpResponse(s)
