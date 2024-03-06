from django.urls import path

from Fruitipedia_app_exam_prep_2.web.views import dashboard, index

urlpatterns = (
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
)