from django.urls import path

from Django_exam_prep_1.web.views import index, create_profile

urlpatterns = (
    path('', index, name='index'),
    path('create-profile/', create_profile, name='create_profile'),
)