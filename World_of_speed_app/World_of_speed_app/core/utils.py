from World_of_speed_app.user_profile.models import Profile


def get_profile():
    return Profile.objects.first()