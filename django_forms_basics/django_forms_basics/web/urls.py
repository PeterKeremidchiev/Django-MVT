from django.urls import path

from django_forms_basics.web.views import index, update_employee

urlpatterns = [
    path('', index, name='index'),
    path('update/<int:pk>/', update_employee, name='update_employee'),
    # path('', redirect_to_softuni, name='redirect_to_softuni'),
]