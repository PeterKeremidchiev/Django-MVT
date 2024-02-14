import random

from django.shortcuts import render


numbers = [random.randint(0, 30) for _ in range(20)]
def index(request):
    context = {
        'numbers': numbers
    }
    return render(request, 'demo_templates/index.html', context)

def about_page(request):
    context = {
        'names': ['Pesho', 'Gosho', 'Ivan', 'Stamat', 'Tosho', 'Petyr']
    }

    return render(request, 'demo_templates/about.html', context)

def show_bootstrap(request):
    context = {
        'has_bootstrap': request.GET.get('has_bootstrap', False)
    }
    return render(request, 'demo_templates/bootstrap.html', context)