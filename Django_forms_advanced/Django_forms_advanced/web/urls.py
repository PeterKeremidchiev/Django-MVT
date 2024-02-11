from django.urls import path

from Django_forms_advanced.web.views import index, create_person, update_person, make_formset

urlpatterns = (
    path('person/update/<int:pk>/', update_person, name='update_person'),
    path('person/create/', create_person, name='create_person'),
    path('form_set/', make_formset, name='form_set'),
    path('', index, name='index'),
)