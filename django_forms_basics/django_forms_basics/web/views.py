from django.shortcuts import render, redirect

from django_forms_basics.web.forms import EmployeeForm
from django_forms_basics.web.models import Employee


# Create your views here.
def index(request):
    if request.method == "GET":
        form = EmployeeForm()
    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('index')

    context = {
        "form": form,
        "employees": Employee.objects.all()
    }

    return render(request, 'web/normal_form.html', context)


def update_employee(request, pk):
    employee = Employee.objects.get(pk=pk)

    if request.method == "GET":
        form = EmployeeForm(instance=employee)
    else:
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        "form": form,
        "employee": employee,
    }

    return render(request, 'web/employee_update.html', context)