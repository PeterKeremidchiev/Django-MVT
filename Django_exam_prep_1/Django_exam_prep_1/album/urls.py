from django.urls import path, include

from Django_exam_prep_1.album.views import CreateAlbumView, DeleteAlbumView, DetailsAlbumView, UpdateAlbumView

urlpatterns = (
    path('add/', CreateAlbumView.as_view(), name='create_album'),
    path('<int:pk>/', include([
        path('delete/', DeleteAlbumView.as_view(), name='delete_album'),
        path('details/', DetailsAlbumView.as_view(), name='details_album'),
        path('edit/', UpdateAlbumView.as_view(), name='edit_album'),
    ]))
)