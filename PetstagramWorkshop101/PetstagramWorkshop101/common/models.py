from django.db import models

from PetstagramWorkshop101.photos.models import Photo


# Create your models here.
class Comment(models.Model):
    TEXT_MAX_LENGTH = 300
    text = models.TextField(max_length=TEXT_MAX_LENGTH)
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='comments')

class Like(models.Model):
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)