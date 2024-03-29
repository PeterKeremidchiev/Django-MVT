# Generated by Django 4.2.10 on 2024-02-23 14:32

import Fruitipedia_app_exam_prep_2.profiles.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, validators=[django.core.validators.MinLengthValidator(2), Fruitipedia_app_exam_prep_2.profiles.validators.name_validator], verbose_name='First Name')),
                ('last_name', models.CharField(max_length=35, validators=[django.core.validators.MinLengthValidator(1), Fruitipedia_app_exam_prep_2.profiles.validators.name_validator], verbose_name='Last Name')),
                ('email', models.EmailField(max_length=40, unique=True, verbose_name='Email')),
                ('password', models.CharField(help_text='*Password length requirements: 8 to 20 characters', max_length=20, validators=[django.core.validators.MinLengthValidator(8)], verbose_name='Password')),
                ('image_url', models.URLField(blank=True, null=True, verbose_name='Image URL')),
                ('age', models.IntegerField(blank=True, default=18, null=True, verbose_name='Age')),
            ],
        ),
    ]
