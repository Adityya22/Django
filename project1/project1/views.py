# from django.http import HttpResponse
from django.shortcuts import render


def HomePage(request):
    data = {
        'title': 'Home',
        'bdata': 'Welcome to Django'
    }
    return render(request, "index.html", data)


def About_Us(request):
    data = {
        'title': 'Home New',
        'bdata': 'Hii everyone'
    }
    return render(request, "first.html", data)


def courses_func(request):
    data = {
        'title': 'Courses',
        'bdata': 'Course Lists',
        "clist": ['php', 'java', 'python'],
        'infolist': [
            {'name': 'Abc', 'city': 'Kolkata'},
            {'name': 'Xyz', 'city': 'Delhi'}
        ],
        'numberlist1': [10, 20, 30, 40, 50],
        'numberlist2': [100, 200, 300, 400, 500]
    }
    return render(request, "courses.html", data)
