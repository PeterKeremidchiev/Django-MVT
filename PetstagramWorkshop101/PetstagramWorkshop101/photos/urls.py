from django.urls import path, include

from PetstagramWorkshop101.photos.views import add_photo_page, photo_details_page, edit_photo_page


urlpatterns = (
    path('add/', add_photo_page, name='add-photo'),
    path('<int:pk>', include([
        path('', photo_details_page, name='photo-details'),
        path('edit/', edit_photo_page, name='edit-photo'),
    ]))

)