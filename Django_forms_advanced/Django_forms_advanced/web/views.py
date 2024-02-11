from django.shortcuts import render, redirect

from Django_forms_advanced.web.forms import PersonForm, PersonForm2, UpdatePersonForm, PersonFormSet
from Django_forms_advanced.web.models import Person


# Create your views here.

def index(request):
    form = PersonForm(request.POST or None)
    form2 = PersonForm2(request.POST)

    context = {
        'form': form,
        'form2': form2,
        'person_list': Person.objects.all()
    }
    return render(request, 'web/index.html', context)

def create_person(request):
    form = PersonForm(request.POST, request.FILES,)
    if form.is_valid():
        form.save()
    return redirect('index')


def update_person(request, pk):
    person = Person.objects.get(pk=pk)
    if request.method == 'GET':
        form = UpdatePersonForm(instance=person)
    else:
        form = UpdatePersonForm(request.POST, request.FILES, instance=person)
        if form.is_valid():
            form.save()
        return redirect('index')
    context = {
        'update_form': form,
        'person': person,
    }
    return render(request, 'web/update_person.html', context)

def make_formset(request):
    form_set = PersonFormSet()
    context = {
        'form_set': form_set,
    }

    return render(request, 'web/formsets.html', context)

