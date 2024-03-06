from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from Fruitipedia_app_exam_prep_2.core.mixins import ProfileFormMixin
from Fruitipedia_app_exam_prep_2.profiles.models import Profile
from Fruitipedia_app_exam_prep_2.web.views import get_profile



class CreateProfileView(ProfileFormMixin, views.CreateView):
    model = Profile
    fields = ('first_name', 'last_name', 'email', 'password')
    template_name = 'profiles/create-profile.html'
    success_url = reverse_lazy('dashboard')

class DetailProfileView(views.DetailView):
    model = Profile
    template_name = 'profiles/details-profile.html'

    def get_object(self, queryset=None):
        return get_profile()

class DeleteProfileView(views.DeleteView):
    model = Profile
    template_name = 'profiles/delete-profile.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_profile()

class EditProfileView(views.UpdateView):
    model = Profile
    fields = ('first_name', 'last_name', 'image_url', 'age')
    template_name = 'profiles/edit-profile.html'
    success_url = reverse_lazy('details_profile')

    def get_object(self, queryset=None):
        return get_profile()





