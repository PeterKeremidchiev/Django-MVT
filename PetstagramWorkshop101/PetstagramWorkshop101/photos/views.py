from django.shortcuts import render, redirect

from PetstagramWorkshop101.common.forms import CommentForm
from PetstagramWorkshop101.photos.forms import PhotoCreateForm, PhotoEditForm
from PetstagramWorkshop101.photos.models import Photo


# Create your views her

# Create your views here.
def add_photo_page(request):
    form = PhotoCreateForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('home')

    context = {
        'form': form,
    }

    return render(request, 'photos/photo-add-page.html', context)


def photo_details_page(request, pk):
    photo = Photo.objects.get(pk=pk)
    comments = photo.comments.all()
    form = CommentForm(request.POST or None)

    context = {
        'pet_photo': photo,
        'comments': comments,
        'comment_form': form,
    }

    return render(request, 'photos/photo-details-page.html', context)


def edit_photo_page(request, pk):
    form = PhotoEditForm(request.POST or None, request.FILES or None)
    photo = Photo.objects.get(pk=pk)
    if form.is_valid():
        form.save()
        return redirect('photo-details')

    context = {
        'form': form,
        'photo': photo,
    }

    return render(request, 'photos/photo-edit-page.html', context)

def photo_delete(request, photo_id):
    photo = Photo.objects.filter(pk=photo_id).first()
    photo.delete()
    return redirect('home')