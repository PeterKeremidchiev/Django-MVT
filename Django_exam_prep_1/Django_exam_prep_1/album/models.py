from django.core.validators import MinValueValidator
from django.db import models

from Django_exam_prep_1.user_profile.models import Profile


# Create your models here.

class Genre(models.TextChoices):
    POP = "Pop Music"
    JAZZ = "Jazz Music"
    ROCK = "Rock Music"
    COUNTRY = "Country Music"
    RNB = "R&B Music"
    DANCE = "Dance Music"
    HIP_HOP = "Hip Hop Music"
    OTHER = "Other"

class Album(models.Model):
    MAX_LENGTH_ALBUM_NAME = 30
    MAX_LENGTH_ARTIST_NAME = 30
    MAX_LENGTH_GENRE = 30
    MIN_PRICE = 0.00

    album_name = models.CharField(
        max_length=MAX_LENGTH_ALBUM_NAME,
        unique=True,
        null=False,
        blank=False,
    )
    artist = models.CharField(
        max_length=MAX_LENGTH_ARTIST_NAME,
        null=False,
        blank=False,
    )
    genre = models.CharField(
        max_length=MAX_LENGTH_GENRE,
        null=False,
        blank=False,
        choices=Genre.choices,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )
    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(MIN_PRICE),
        )
    )
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )