from django.urls import reverse_lazy, reverse
from django.views import generic as views
from django.shortcuts import render, redirect

from PetstagramWorkshop101.common.forms import CommentForm
from PetstagramWorkshop101.photos.forms import PhotoCreateForm, PhotoEditForm
from PetstagramWorkshop101.photos.models import Photo


class CreatePhotoView(views.CreateView):
    queryset = Photo.objects.all() \
        .prefetch_related("pets")
    form_class = PhotoCreateForm
    template_name = 'photos/photo-add-page.html'
    # success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse("photo-details", kwargs={
            "pk": self.object.pk,
        })

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.instance.user = self.request.user
        return form

class DetailsPhotoView(views.DetailView):
    model = Photo
    template_name = 'photos/photo-details-page.html'
    context_object_name = 'pet_photo'
    pk_url_kwarg = 'pk'

    def get_object(self, queryset=None):
        return Photo.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['comment_form'] = CommentForm
        return context

class EditPhotoView(views.UpdateView):
    model = Photo
    form_class = PhotoEditForm
    template_name = 'photos/photo-edit-page.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'photo'

    def get_success_url(self):
        return reverse("photo-details", kwargs={
            "pk": self.object.pk,
        })

def photo_delete(request, photo_id):
    photo = Photo.objects.filter(pk=photo_id).first()
    photo.delete()
    return redirect('home')