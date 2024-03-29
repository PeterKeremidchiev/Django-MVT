# Generated by Django 4.2.10 on 2024-02-23 14:44

import Fruitipedia_app_exam_prep_2.fruits.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'unique': 'This fruit name is already in use! Try a new one.'}, max_length=30, unique=True, validators=[django.core.validators.MinLengthValidator(2), Fruitipedia_app_exam_prep_2.fruits.validators.fruit_name_validator])),
                ('image_url', models.URLField()),
                ('description', models.TextField()),
                ('nutrition', models.TextField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
        ),
    ]
