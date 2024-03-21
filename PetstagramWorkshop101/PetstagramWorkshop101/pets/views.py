from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from PetstagramWorkshop101.common.forms import CommentForm
from PetstagramWorkshop101.pets.forms import PetForm, PetEditForm, PetDeleteForm
from PetstagramWorkshop101.pets.models import Pet
from django.views import generic as views

# Create your views here.

class CreatePetView(views.CreateView):
    model = Pet
    form_class = PetForm
    template_name = 'pets/pet-add-page.html'
    success_url = reverse_lazy('show-profile-details', kwargs={'pk': 1})

class DetailsPetView(views.DetailView):
    model = Pet
    template_name = 'pets/pet-details-page.html'
    context_object_name = 'pet'
    slug_url_kwarg = 'pet_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_photos'] = self.object.photo_set.all()
        context['comment_form'] = CommentForm
        return context


class DeletePetView(views.DeleteView):
    model = Pet
    template_name = 'pets/pet-delete-page.html'
    context_object_name = 'pet'
    success_url = reverse_lazy('show-profile-details', kwargs={'pk': 1})

    def get_object(self, queryset=None):
        return Pet.objects.get(slug=self.kwargs['pet_slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PetDeleteForm(initial=self.object.__dict__)
        context['username'] = 'archey'
        return context

    def delete(self, request, *args, **kwargs):
        pet = self.get_object()
        pet.delete()
        return redirect(self.success_url)
class EditPetView(views.UpdateView):
    model = Pet
    form_class = PetEditForm
    template_name = 'pets/pet-edit-page.html'
    slug_url_kwarg = 'pet_slug'
    context_object_name = 'pet'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["username"] = "Rexy"
        return context
    def get_success_url(self):
        return reverse_lazy(
            'pet-details',
            kwargs={'username': self.kwargs['username'], 'pet_slug': self.kwargs['pet_slug']},
        )
