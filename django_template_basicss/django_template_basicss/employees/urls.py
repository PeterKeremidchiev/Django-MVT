from django.urls import path

from django_template_basicss.employees.views import index, employee_details

urlpatterns = [
    path('', index, name='index'),
    path('employees/<pk>/', employee_details, name='employee_details'),
]