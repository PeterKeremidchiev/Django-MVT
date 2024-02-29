from django.core.validators import MinLengthValidator
from django.db import models

from Fruitipedia_app_exam_prep_2.profiles.validators import name_validator


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 25
    FIRST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 35
    LAST_NAME_MIN_LENGTH = 1
    EMAIL_MAX_LENGTH = 40
    PASSWORD_MIN_LENGTH = 8
    PASSWORD_MAX_LENGTH = 20


    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            name_validator,
        ),
        null=False,
        blank=False,

    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            name_validator,
        ),
        null=False,
        blank=False,
        verbose_name='Last Name'
    )
    email = models.EmailField(
        max_length=EMAIL_MAX_LENGTH,
        unique=True,
        null=False,
        blank=False,
        verbose_name='Email'
    )
    password = models.CharField(
        max_length=PASSWORD_MAX_LENGTH,
        validators=(
            MinLengthValidator(PASSWORD_MIN_LENGTH),
        ),
        null=False,
        blank=False,
        help_text="*Password length requirements: 8 to 20 characters",
        verbose_name='Password'
    )
    image_url = models.URLField(
        null=True,
        blank=True,
        verbose_name='Image URL',
    )
    age = models.IntegerField(
        null=True,
        blank=True,
        default=18,
        verbose_name='Age'
    )