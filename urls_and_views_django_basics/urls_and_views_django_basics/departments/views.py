from django.shortcuts import render
from django.template import context


# Create your views here.
def search_departments_multiple_params(request, pk, name, id):
    context = {
        'pk': pk,
        "name": name,
        "id": id,
    }
    return render(request, 'departments/index.html', context)

