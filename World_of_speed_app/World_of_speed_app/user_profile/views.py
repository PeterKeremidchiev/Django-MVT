from django import forms
from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render

from World_of_speed_app.core.mixins import GetProfileObjectMixin
from World_of_speed_app.core.utils import get_profile
from World_of_speed_app.user_profile.models import Profile


# Create your views here.


class CreateProfileView(views.CreateView):
    queryset = Profile.objects.all()
    fields = ('username', 'email', 'age', 'password')
    template_name = 'user_profile/profile-create.html'
    success_url = reverse_lazy('catalogue')

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.fields['password'].widget = forms.PasswordInput()
        return form

class DetailsProfileView(GetProfileObjectMixin, views.DetailView):
    queryset = Profile.objects.all()
    template_name = 'user_profile/profile-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_price'] = sum([car.price for car in self.object.car_set.all()])
        return context

class EditProfileView(GetProfileObjectMixin, views.UpdateView):
    queryset = Profile.objects.all()
    fields = ('username', 'email', 'age', 'password', 'first_name', 'last_name', 'profile_picture')
    template_name = 'user_profile/profile-edit.html'
    success_url = reverse_lazy('details_profile')



class DeleteProfileView(GetProfileObjectMixin, views.DeleteView):
    queryset = Profile.objects.all()
    template_name = 'user_profile/profile-delete.html'
    success_url = reverse_lazy('index')

