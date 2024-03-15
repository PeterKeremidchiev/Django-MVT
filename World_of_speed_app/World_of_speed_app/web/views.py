from django.shortcuts import render

from World_of_speed_app.core.utils import get_profile
from World_of_speed_app.user_profile.models import Profile


# Create your views here.


def index(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }
    return render(request, 'web/index.html', context)