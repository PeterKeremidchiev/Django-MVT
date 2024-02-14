from django.urls import path

from Templates_advanced.demo_templates.views import index, about_page, show_bootstrap

urlpatterns = (
    path('about/', about_page, name='about_page'),
    path('bootstrap/', show_bootstrap, name='show_bootstrap'),
    path('', index, name='index'),

)