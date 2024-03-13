from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator

from World_of_speed_app.user_profile.validators import username_validator



class Profile(models.Model):
    MAX_USERNAME_LENGTH = 15
    MIN_USERNAME_LENGTH = 3
    MIN_VALUE_AGE = 21
    MAX_PASSWORD_LENGTH = 20
    MAX_FIRST_NAME_LENGTH = 25
    MAX_LAST_NAME_LENGTH = 25

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_USERNAME_LENGTH, "Username must be at least 3 chars long!"),
            username_validator,
        ),
        null=False,
        blank=False,
    )
    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.IntegerField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(MIN_VALUE_AGE),
        ),
        help_text="Age requirement: 21 years and above."
    )
    password = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_PASSWORD_LENGTH,
    )
    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_FIRST_NAME_LENGTH,
    )
    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_LAST_NAME_LENGTH,
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )
