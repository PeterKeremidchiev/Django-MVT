from django.urls import path, include


from Fruitipedia_app_exam_prep_2.fruits.views import CreateFruitView, DetailsFruitView, EditFruitView, DeleteFruitView

urlpatterns = (
    path('create/', CreateFruitView.as_view(), name='create_fruit'),
    path('<int:fruit_id>/', include([
        path('details/', DetailsFruitView.as_view(), name='details_fruit'),
        path('edit/', EditFruitView.as_view(), name='edit_fruit'),
        path('delete/', DeleteFruitView.as_view(), name='delete_fruit'),
    ]))
)