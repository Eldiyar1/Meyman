# Generated by Django 4.2.3 on 2023-08-24 09:59

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housingreservation',
            name='check_in_date',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 8, 24))], verbose_name='Заезд'),
        ),
        migrations.AlterField(
            model_name='housingreservation',
            name='check_out_date',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 8, 24))], verbose_name='Выезд'),
        ),
        migrations.CreateModel(
            name='HousingAvailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('is_available', models.BooleanField(default=True)),
                ('housing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='availability', to='travel.housing', verbose_name='Место жительство')),
            ],
            options={
                'verbose_name': 'Календарь',
                'verbose_name_plural': 'Календари',
                'unique_together': {('housing', 'date')},
            },
        ),
    ]