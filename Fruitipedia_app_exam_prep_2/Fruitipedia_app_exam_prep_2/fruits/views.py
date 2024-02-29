from django.forms import modelform_factory
from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render

from Fruitipedia_app_exam_prep_2.core.mixins import FruitFormMixin, DisabledFormMixin
from Fruitipedia_app_exam_prep_2.fruits.models import Fruit
from Fruitipedia_app_exam_prep_2.web.views import get_profile


# Create your views here.
class CreateFruitView(FruitFormMixin, views.CreateView):
    queryset = Fruit.objects.all()
    fields = ('name', 'image_url', 'description', 'nutrition')
    template_name = 'fruits/create-fruit.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.owner_id = get_profile().pk
        return super().form_valid(form)

class DetailsFruitView(views.DetailView):
    queryset = Fruit.objects.all()
    template_name = 'fruits/details-fruit.html'

    def get_object(self, queryset=None):

        return self.get_queryset().get(pk=self.kwargs['fruit_id'])

class EditFruitView(views.UpdateView):
    queryset = Fruit.objects.all()
    fields = ('name', 'image_url', 'description', 'nutrition')
    template_name = 'fruits/edit-fruit.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self, queryset=None):

        return self.get_queryset().get(pk=self.kwargs['fruit_id'])

class DeleteFruitView(DisabledFormMixin, views.DeleteView):
    queryset = Fruit.objects.all()
    template_name = 'fruits/delete-fruit.html'
    success_url = reverse_lazy('dashboard')
    form_class = modelform_factory(
        Fruit,
        fields=('name', 'image_url', 'description')
    )
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object
        return kwargs

    def get_object(self, queryset=None):

        return self.get_queryset().get(pk=self.kwargs['fruit_id'])