from django.urls import path

from PetstagramWorkshop101.common.views import home_page, like_functionality, share_functionality, comment_functionality

urlpatterns = (
    path('', home_page, name='home'),
    path('like/<int:photo_id>/', like_functionality, name='like'),
    path('share/<int:photo_id>/', share_functionality, name='share'),
    path('comment/<int:photo_id>/', comment_functionality, name='comment'),
)