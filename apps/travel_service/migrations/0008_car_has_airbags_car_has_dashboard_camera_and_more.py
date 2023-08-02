# Generated by Django 4.2.3 on 2023-08-01 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_service', '0007_remove_car_has_airbags_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='has_airbags',
            field=models.BooleanField(default=False, verbose_name='Наличие подушка безопасности'),
        ),
        migrations.AddField(
            model_name='car',
            name='has_dashboard_camera',
            field=models.BooleanField(default=False, verbose_name='Наличие авторегистратора'),
        ),
        migrations.AddField(
            model_name='car',
            name='has_emergency_tools',
            field=models.BooleanField(default=False, verbose_name='Наличие инструментов аварийной ситуации'),
        ),
        migrations.AddField(
            model_name='car',
            name='has_fire_extinguisher',
            field=models.BooleanField(default=False, verbose_name='Наличие огнетушителя'),
        ),
        migrations.AddField(
            model_name='car',
            name='has_first_aid_kit',
            field=models.BooleanField(default=False, verbose_name='Наличие аптечки'),
        ),
        migrations.AddField(
            model_name='car',
            name='has_spare_wheel',
            field=models.BooleanField(default=False, verbose_name='Наличие запасного колеса'),
        ),
    ]
