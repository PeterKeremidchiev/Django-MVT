from django.urls import path, include

from PetstagramWorkshop101.accounts.views import register_page, login_page, show_profile_details, edit_profile, \
    delete_profile, sign_out_page

urlpatterns = (
    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
    path("signout/", sign_out_page, name="signout-page"),

    path('profile/<int:pk>/', include([
        path('', show_profile_details, name='show-profile-details'),
        path('edit/', edit_profile, name='edit-profile'),
        path('delete/', delete_profile, name='delete-profile'),
    ])),
)