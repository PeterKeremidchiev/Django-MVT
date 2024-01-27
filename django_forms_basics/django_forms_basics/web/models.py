from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.


def non_empty_spaces(value):
    if " " in value:
        raise ValidationError(message='Spaces in this field are not allowed')
class Employee(models.Model):
    MAX_FIRST_LAST_NAME_LENGTH = 35
    ROLES = (
        (1, 'Software Developer'),
        (2, 'QA engineer'),
        (3, 'Project Manager'),
    )
    first_name = models.CharField(
        max_length=MAX_FIRST_LAST_NAME_LENGTH,
        null=False,
        blank=False,
        validators=[non_empty_spaces]
    )

    last_name = models.CharField(
        max_length=MAX_FIRST_LAST_NAME_LENGTH,
        null=False,
        blank=False,
    )

    role = models.IntegerField(
        choices=ROLES,
        null=False,
        blank=False,
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
