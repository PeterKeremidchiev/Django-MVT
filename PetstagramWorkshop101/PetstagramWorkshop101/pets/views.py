from django.shortcuts import render, redirect

from PetstagramWorkshop101.common.forms import CommentForm
from PetstagramWorkshop101.pets.forms import PetForm, PetEditForm, PetDeleteForm
from PetstagramWorkshop101.pets.models import Pet


# Create your views here.
def create_pet(request):
    form = PetForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('show-profile-details', pk=1)

    context = {
        'form': form
    }
    return render(request, 'pets/pet-add-page.html', context)

def pet_details(request, username, pet_slug):
    form = CommentForm(request.POST or None)
    context = {
        "pet": Pet.objects.get(slug=pet_slug),
        "comment_form": form,
    }

    return render(request, 'pets/pet-details-page.html', context)

def pet_delete(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    form = PetDeleteForm(request.POST or None, instance=pet)

    if request.method == "POST":
        pet.delete()
        return redirect('home')


    context = {
        'form': form
    }

    return render(request, 'pets/pet-delete-page.html', context)

def pet_edit(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)

    if request.method == "GET":
        form = PetEditForm(instance=pet, initial=pet.__dict__)
    else:
        form = PetEditForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet-details', username=username, pet_slug=pet_slug)

    context = {
        'form': form,
    }

    return render(request, 'pets/pet-edit-page.html', context)