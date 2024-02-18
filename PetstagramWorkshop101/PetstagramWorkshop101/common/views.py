from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from PetstagramWorkshop101.common.forms import CommentForm, SearchForm
from PetstagramWorkshop101.common.models import Like
from PetstagramWorkshop101.photos.models import Photo


# Create your views here.
def home_page(request):
    form = CommentForm(request.POST or None)
    search_form = SearchForm(request.GET or None)
    photos = Photo.objects.all()

    if search_form.is_valid():
        photos = photos.filter(
            tagged_pets__name__icontains=search_form.cleaned_data['pet_name'],
        )

    context = {
        'pet_photos': photos,
        'comment_form': form,
        'search_form': search_form,
    }

    return render(request, 'common/home-page.html', context)

def like_functionality(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    liked_object = Like.objects.filter(to_photo_id=photo_id).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_photo=photo)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#photo-{photo_id}')

def share_functionality(request, photo_id):
    copy(request.META['HTTP_HOST'] + resolve_url('photo-details', photo_id))

    return redirect(request.META['HTTP_REFERER'] + f'#photo-{photo_id}')

def comment_functionality(request, photo_id):
    if request.method == 'POST':
        photo = Photo.objects.get(id=photo_id)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.save()

        return redirect(request.META['HTTP_REFERER'] + f'#photo-{photo_id}')