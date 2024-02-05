from django.contrib import admin

from PetstagramWorkshop101.pets.models import Pet


# Register your models here.
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')