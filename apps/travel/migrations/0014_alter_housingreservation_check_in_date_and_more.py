# Generated by Django 4.2.3 on 2023-09-06 19:00

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0013_remove_housingreservation_teens'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housingreservation',
            name='check_in_date',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 9, 6))], verbose_name='Заезд'),
        ),
        migrations.AlterField(
            model_name='housingreservation',
            name='check_out_date',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 9, 6))], verbose_name='Выезд'),
        ),
    ]