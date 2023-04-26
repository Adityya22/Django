# from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.
def welcome(request):
    s = '<h1 style="color:blue" align=center> Django Application </h1>'
    return HttpResponse(s)


def timeinfo(request):
    date = datetime.datetime.now()
    msg = '<h1> hello good evening </h1><hr>'
    msg = msg + 'Now the server time is: '+str(date)
    return HttpResponse(msg)
