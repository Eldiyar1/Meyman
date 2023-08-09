# Generated by Django 4.2.3 on 2023-08-08 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('review', '0002_initial'),
        ('travel_service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='transfer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review_travel_service', to='travel_service.transfer', verbose_name='Трэвел-услуги'),
        ),
    ]
