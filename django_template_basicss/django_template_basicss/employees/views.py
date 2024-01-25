import datetime

from django.shortcuts import render
from django.shortcuts import render
from django.urls import reverse
# Create your views here.

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
def index(request):
    person = Person('Peter', 'Spielberg', 80)
    context = {
        'title': 'Employees',
        'employees': ['Tom', 'John', 'Bill', 'Sam'],
        'date': datetime.datetime.now(),
        'director': {
            'first_name': 'Steven',
            'last_name': 'Spielberg',
            'age': 60
        },
        'person_object': person,

    }
    return render(request, 'employees/index.html', context)


def employee_details(request, pk):
    context = {
        'title': 'Employee Details',
        'pk': pk,

    }
    return render(request, 'employees/details.html', context)