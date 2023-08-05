# Generated by Django 4.2.3 on 2023-08-05 08:31

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accommodationreservation',
            name='check_in_date',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 8, 5))], verbose_name='Заезд'),
        ),
        migrations.AlterField(
            model_name='accommodationreservation',
            name='check_out_date',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 8, 5))], verbose_name='Выезд'),
        ),
        migrations.AlterField(
            model_name='carreservation',
            name='check_in_date',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 8, 5))], verbose_name='дата бронирование'),
        ),
        migrations.AlterField(
            model_name='carreservation',
            name='check_out_date',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 8, 5))]),
        ),
    ]
