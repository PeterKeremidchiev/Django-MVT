from django.core.validators import MinLengthValidator
from django.db import models

from Fruitipedia_app_exam_prep_2.fruits.validators import fruit_name_validator
from Fruitipedia_app_exam_prep_2.profiles.models import Profile


# Create your models here.
class Fruit(models.Model):
    MAX_NAME_LENGTH = 30
    MIN_NAME_LENGTH = 2
    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_NAME_LENGTH),
            fruit_name_validator,
        ),
        unique=True,
        null=False,
        blank=False,
        error_messages={
            'unique': 'This fruit name is already in use! Try a new one.'
        },
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )
    description = models.TextField(
        null=False,
        blank=False,
    )
    nutrition = models.TextField(
        null=True,
        blank=True,
    )
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )