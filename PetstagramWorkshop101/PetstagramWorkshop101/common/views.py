from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from PetstagramWorkshop101.common.forms import CommentForm, SearchForm
from PetstagramWorkshop101.common.models import Like
from PetstagramWorkshop101.photos.models import Photo
from django.views import generic as views


# Create your views here.
class HomePageView(views.ListView):
    model = Photo
    template_name = 'common/home-page.html'
    context_object_name = 'pet_photos'
    paginate_by = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm
        context['search_form'] = SearchForm
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        pet_name = self.request.GET.get('pet_name')

        if pet_name:
            self.request.session['pet_name'] = pet_name
        else:
            self.request.session.pop('pet_name', None)

        pet_name_session = self.request.session.get('pet_name')

        if pet_name:
            queryset = queryset.filter(
                tagged_pets__name__icontains=pet_name_session
            )

        return queryset
# def home_page(request):
#     form = CommentForm(request.POST or None)
#     search_form = SearchForm(request.GET or None)
#     photos = Photo.objects.all()
#
#     if search_form.is_valid():
#         photos = photos.filter(
#             tagged_pets__name__icontains=search_form.cleaned_data['pet_name'],
#         )
#
#     photos_per_page = 1
#     paginator = Paginator(photos, photos_per_page)
#     page = request.GET.get('page')
#
#     try:
#         photos = paginator.page(page)
#     except PageNotAnInteger:
#         photos = paginator.page(1)
#     except EmptyPage:
#         photos = paginator.page(paginator.num_pages)
#
#     context = {
#         'pet_photos': photos,
#         'comment_form': form,
#         'search_form': search_form,
#     }
#
#     return render(request, 'common/home-page.html', context)

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