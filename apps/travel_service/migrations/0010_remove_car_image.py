# Generated by Django 4.2.3 on 2023-08-01 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel_service', '0009_remove_car_has_airbags_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='image',
        ),
    ]
