from django.urls import path

from urls_and_views_django_basics.departments.views import search_departments_multiple_params

urlpatterns = (
    path('<int:pk>/<str:name>/<slug:id>/', search_departments_multiple_params, name='search_departments_multiple_params'),
)
