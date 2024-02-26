from django.shortcuts import render, redirect

from Django_exam_prep_1.album.models import Album
from Django_exam_prep_1.user_profile.models import Profile
from Django_exam_prep_1.web.forms import CreateProfileForm



def get_profile():
    return Profile.objects.first()
def create_profile(request):
    form = CreateProfileForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form': form,
        'no_nav': True,
    }
    return render(request, 'web/home-no-profile.html', context)


def index(request):
    profile = get_profile()

    if profile is None:
        return create_profile(request)

    context = {
        'albums': Album.objects.all(),
    }
    return render(request, 'web/home-with-profile.html', context)

