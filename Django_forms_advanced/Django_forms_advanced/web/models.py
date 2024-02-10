from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
class Person(models.Model):
    MAX_FIRSTNAME_LENGTH = 35
    MAX_LASTNAME_LENGTH = 35
    first_name = models.CharField(max_length=MAX_FIRSTNAME_LENGTH, validators=(MinLengthValidator(2),))
    last_name = models.CharField(max_length=MAX_LASTNAME_LENGTH, validators=(MinLengthValidator(2),))
    age = models.IntegerField()
    profile_image = models.ImageField(upload_to='web/profile_images', null=True, blank=True)