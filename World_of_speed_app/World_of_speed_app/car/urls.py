from django.urls import path, include

from World_of_speed_app.car.views import catalogue, CreateCarView, DetailsCarView, EditCarView, DeleteCarView

urlpatterns = (
    path('catalogue/', catalogue, name='catalogue'),
    path('create/', CreateCarView.as_view(), name='create_car'),
    path('<int:id>/', include([
        path('details/', DetailsCarView.as_view(), name='details_car'),
        path('edit/', EditCarView.as_view(), name='edit_car'),
        path('delete/', DeleteCarView.as_view(), name='delete_car'),
    ]))
)