# Generated by Django 4.2.3 on 2023-08-05 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel_service', '0009_rename_has_safety_equipment_transfer_safety_equipment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transferreservation',
            name='user',
        ),
    ]
