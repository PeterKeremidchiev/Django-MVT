from django.shortcuts import render, redirect

from Fruitipedia_app_exam_prep_2.profiles.models import Profile
from Fruitipedia_app_exam_prep_2.fruits.models import Fruit


def get_profile():
    return Profile.objects.first()
def index(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'web/index.html', context)

def dashboard(request):
    profile = get_profile()

    if profile is None:
        return index(request)
    context = {
        'profile': profile,
        'fruits': Fruit.objects.all(),
    }
    return render(request, 'web/dashboard.html', context)