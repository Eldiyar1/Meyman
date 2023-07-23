# Generated by Django 4.2.3 on 2023-07-23 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_accommodationreservation_payment_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accommodationreservation',
            name='booking_type',
            field=models.IntegerField(choices=[('Без банковской карты', 'Без банковской карты'), ('Бесплатная отмена', 'Бесплатная отмена')], default=1, verbose_name='Бронирование'),
        ),
    ]
