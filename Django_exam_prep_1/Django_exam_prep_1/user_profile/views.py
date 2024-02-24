from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render

from Django_exam_prep_1.user_profile.models import Profile
from Django_exam_prep_1.web.views import get_profile


# Create your views here.
class DetailProfileView(views.DetailView):
    template_name = 'profile/profile-details.html'

    def get_object(self, queryset=None):
        return get_profile()

class DeleteProfileView(views.DeleteView):
    template_name = 'profile/profile-delete.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_profile()