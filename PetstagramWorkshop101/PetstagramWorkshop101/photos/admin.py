from django.contrib import admin

from PetstagramWorkshop101.photos.models import Photo


# Register your models here.
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_of_publication', 'description', 'get_tagged_pets', 'get_comments')

    @staticmethod
    def get_tagged_pets(obj):
        return ', '.join([pet.name for pet in obj.tagged_pets.all()])

    @staticmethod
    def get_comments(obj):
        return ', '.join([comment.text for comment in obj.comments.all()])