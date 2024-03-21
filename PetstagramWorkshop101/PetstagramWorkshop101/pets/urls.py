from django.conf.urls.static import static
from django.urls import path, include

from django.conf import settings
from PetstagramWorkshop101.pets.views import CreatePetView, DetailsPetView, EditPetView, DeletePetView

urlpatterns = [
    path('add/', CreatePetView.as_view(), name='create-pet'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', DetailsPetView.as_view(), name='pet-details'),
        path('edit/', EditPetView.as_view(), name='pet-edit'),
        path('delete/', DeletePetView.as_view(), name='pet-delete'),
    ]))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)