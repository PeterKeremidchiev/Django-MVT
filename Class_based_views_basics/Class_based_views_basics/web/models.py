from django.db import models
from django.core.validators import MinLengthValidator

class Category(models.Model):
    MIN_NAME_LENGTH = 2
    MAX_NAME_LENGTH = 35
    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_NAME_LENGTH),
        )
    )

    def __str__(self):
        return self.name

# Create your models here.
class TodoList(models.Model):
    MAX_TITLE_LENGTH = 45
    MIN_TITLE_LENGTH = 3
    title = models.CharField(
        max_length=MAX_TITLE_LENGTH,
        validators=[
        MinLengthValidator(MIN_TITLE_LENGTH)],
        null=False,
        blank=False
    )

    deadline = models.DateTimeField(
        null=True,
        blank=True,
    )

    date_created = models.DateTimeField(
        auto_now_add=True,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )