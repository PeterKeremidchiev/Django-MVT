from django.urls import path

from PetstagramWorkshop101.common.views import home_page

urlpatterns = (
    path('', home_page, name='home'),
)