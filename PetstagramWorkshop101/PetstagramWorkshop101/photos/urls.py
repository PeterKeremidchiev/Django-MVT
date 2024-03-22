from django.urls import path, include

from PetstagramWorkshop101.photos.views import photo_delete, CreatePhotoView, DetailsPhotoView, EditPhotoView

urlpatterns = (
    path('add/', CreatePhotoView.as_view(), name='add-photo'),
    path('<int:pk>/', include([
        path('', DetailsPhotoView.as_view(), name='photo-details'),
        path('edit/', EditPhotoView.as_view(), name='edit-photo'),
        path('delete/<int:photo_id>', photo_delete, name='delete-photo'),
    ]))

)