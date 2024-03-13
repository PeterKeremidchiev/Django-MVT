from django.urls import path

from World_of_speed_app.user_profile.views import CreateProfileView, DetailsProfileView, EditProfileView, \
    DeleteProfileView

urlpatterns = (
    path('create/', CreateProfileView.as_view(), name='create_profile'),
    path('details/', DetailsProfileView.as_view(), name='details_profile'),
    path('edit/', EditProfileView.as_view(), name='edit_profile'),
    path('delete/', DeleteProfileView.as_view(), name='delete_profile'),
)