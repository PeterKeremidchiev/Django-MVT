from django.forms import modelform_factory
from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render, redirect

from World_of_speed_app.car.models import Car
from World_of_speed_app.core.mixins import ReadOnlyMixin, GetCarContextDataMixin
from World_of_speed_app.core.utils import get_profile

def catalogue(request):
    profile = get_profile()

    if profile is None:
        return redirect('index')
    context = {
        'profile': profile,
        'cars': Car.objects.all(),
    }
    return render(request, 'car/catalogue.html', context)

class CreateCarView(GetCarContextDataMixin, views.CreateView):
    queryset = Car.objects.all()
    fields = ('type', 'model', 'year', 'image_url', 'price')
    template_name = 'car/car-create.html'
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        form.instance.owner_id = get_profile().pk
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.fields['image_url'].widget.attrs['placeholder'] = 'https://...'
        return form

class DetailsCarView(GetCarContextDataMixin, views.DetailView):
    queryset = Car.objects.all()
    template_name = 'car/car-details.html'

    def get_object(self, queryset=None):

        return self.get_queryset().get(pk=self.kwargs['id'])

class EditCarView(GetCarContextDataMixin, views.UpdateView):
    queryset = Car.objects.all()
    fields = ('type', 'model', 'year', 'image_url', 'price')
    template_name = 'car/car-edit.html'
    success_url = reverse_lazy('catalogue')

    def get_object(self, queryset=None):

        return self.get_queryset().get(pk=self.kwargs['id'])

class DeleteCarView(ReadOnlyMixin, GetCarContextDataMixin, views.DeleteView):
    queryset = Car.objects.all()
    template_name = 'car/car-delete.html'
    success_url = reverse_lazy('catalogue')
    form_class = modelform_factory(
        Car,
        fields=('type', 'model', 'year', 'image_url', 'price')
    )

    def get_object(self, queryset=None):

        return self.get_queryset().get(pk=self.kwargs['id'])

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object
        return kwargs


