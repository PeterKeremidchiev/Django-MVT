from django.urls import path

from urls_and_views_django_basics.core.views import response_to_pk, response_for_empty_path, response_with_str, \
    response_to_name_and_pk, redirect_to_softuni, raise_error, raise_exception

urlpatterns = (
    path('raise_error/', raise_error, name='raise_error_with_response'),
    path('raise_exception/', raise_exception, name='raise_exception'),
    path('to-softuni/', redirect_to_softuni),
    path('<int:pk>/', response_to_pk, name='response_to_pk'),
    path('<str:name>', response_with_str, name='response_with_str'),
    path('<str:name>/<int:pk>/', response_to_name_and_pk, name='response_to_name_and_pk'),

    path('', response_for_empty_path, name='empty_response'),
)

