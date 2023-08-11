# Generated by Django 4.2.3 on 2023-08-11 06:06

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0022_alter_room_bed_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housingreservation',
            name='check_in_date',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 8, 11))], verbose_name='Заезд'),
        ),
        migrations.AlterField(
            model_name='housingreservation',
            name='check_out_date',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 8, 11))], verbose_name='Выезд'),
        ),
    ]
