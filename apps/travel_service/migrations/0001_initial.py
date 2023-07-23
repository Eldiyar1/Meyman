

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(choices=[('Бишкек', 'Бишкек'), ('Джалал-Абад', 'Джалал-Абад'), ('Иссык-Куль', 'Иссык-Куль'), ('Ош', 'Ош'), ('Нарын', 'Нарын'), ('Талас', 'Талас'), ('Баткен', 'Баткен')], max_length=100, verbose_name='Куда')),
                ('check_in_date', models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 7, 22))], verbose_name='Заезд')),
                ('check_out_date', models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 7, 22))], verbose_name='Выезд')),

                ('adults', models.PositiveIntegerField(default=1, verbose_name='Взрослые(от 18 лет)')),
                ('teens', models.PositiveIntegerField(default=0, verbose_name='Подростки(от 13-18 лет)')),
                ('children', models.PositiveIntegerField(default=0, verbose_name='Дети(от 2-12 лет)')),
                ('infants', models.PositiveIntegerField(default=0, verbose_name='Младенцы(младше 2)')),
                ('pets', models.PositiveIntegerField(default=0, verbose_name='Домашние животные')),
            ],
            options={
                'verbose_name': 'Поиск жилья',
                'verbose_name_plural': 'Поиск жилья',
            },
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

                ('transfer_location', models.CharField(max_length=255, verbose_name='Место получения трансфера')),
                ('pickup_date', models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 7, 22))], verbose_name='Дата получения трансфера')),
                ('pickup_time', models.TimeField(verbose_name='Время получения трансфера')),
                ('return_location', models.CharField(max_length=255, verbose_name='Место возврата трансфера')),
                ('return_date', models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 7, 22))], verbose_name='Дата возврата трансфера')),
                ('return_time', models.TimeField(verbose_name='Время возврата трансфера')),
                ('different_pickup_places', models.BooleanField(default=False, verbose_name='Разные места получения')),
                ('with_driver', models.BooleanField(default=False, verbose_name='Трансфер с водителем')),
            ],
            options={
                'verbose_name': 'Поиск трансфера',
                'verbose_name_plural': 'Поиск Трансферов',
            },
        ),
    ]
