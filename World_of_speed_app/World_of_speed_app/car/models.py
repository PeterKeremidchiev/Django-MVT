from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from World_of_speed_app.user_profile.models import Profile


# Create your models here.
class Type(models.TextChoices):
    RALLY = "Rally"
    OPEN_WHEEL = "Open-Wheel"
    KART = "Kart"
    DRAG = "Drag"
    OTHER = "Other"

class Car(models.Model):
    MAX_TYPE_LENGTH = 10
    MAX_MODEL_LENGTH = 15
    MIN_MODEL_LENGTH = 1
    MIN_PRICE = 1.0

    type = models.CharField(
        max_length=MAX_TYPE_LENGTH,
        null=False,
        blank=False,
        choices=Type.choices,
    )
    model = models.CharField(
        max_length=MAX_MODEL_LENGTH,
        validators=[
            MinLengthValidator(MIN_MODEL_LENGTH)
        ],
        null=False,
        blank=False,
    )
    year = models.IntegerField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(1999, message="Year must be between 1999 and 2030!"),
            MaxValueValidator(2030, message="Year must be between 1999 and 2030!"),
        ],
    )
    image_url = models.URLField(
        unique=True,
        null=False,
        blank=False,
        error_messages={
            'unique': 'This image URL is already in use! Provide a new one.'
        },

    )
    price = models.FloatField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(MIN_PRICE)
        ],
    )
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )