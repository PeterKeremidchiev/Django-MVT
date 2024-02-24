from django.urls import path

from Django_exam_prep_1.user_profile.views import DetailProfileView, DeleteProfileView

urlpatterns = (
    path('details/', DetailProfileView.as_view(), name='profile_details'),
    path('delete/', DeleteProfileView.as_view(), name='profile_delete'),
)