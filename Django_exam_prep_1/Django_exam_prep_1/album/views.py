from django.forms import modelform_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from Django_exam_prep_1.album.models import Album
from Django_exam_prep_1.common.mixins import AlbumFormViewMixin, ReadonlyViewMixin
from Django_exam_prep_1.web.views import get_profile



class CreateAlbumView(AlbumFormViewMixin, views.CreateView):
    queryset = Album.objects.all()
    fields = ('album_name', 'artist', 'genre', 'description', 'image_url', 'price')
    template_name = 'album/album-add.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.owner_id = get_profile().pk
        return super().form_valid(form)

class DetailsAlbumView(views.DetailView):
    queryset = Album.objects.all()
    template_name = 'album/album-details.html'

class UpdateAlbumView(AlbumFormViewMixin, views.UpdateView):
    queryset = Album.objects.all()
    fields = ('album_name', 'artist', 'genre', 'description', 'image_url', 'price')
    template_name = 'album/album-edit.html'
    success_url = reverse_lazy('index')

class DeleteAlbumView(ReadonlyViewMixin, views.DeleteView):
    queryset = Album.objects.all()
    template_name = 'album/album-delete.html'
    success_url = reverse_lazy('index')
    form_class = modelform_factory(
        Album,
        fields=('album_name', 'artist', 'genre', 'description', 'image_url', 'price'),
    )

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object
        return kwargs