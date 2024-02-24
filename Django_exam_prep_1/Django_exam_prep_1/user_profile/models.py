from django.core.validators import MinLengthValidator
from django.db import models

from Django_exam_prep_1.common.validators import username_validator

class Profile(models.Model):
    MAX_LENGTH_USERNAME = 15
    MIN_LENGTH_USERNAME = 2
    username = models.CharField(
        max_length=MAX_LENGTH_USERNAME,
        validators=(
            MinLengthValidator(MIN_LENGTH_USERNAME),
            username_validator,
        ),
        null=False,
        blank=False,
    )
    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )