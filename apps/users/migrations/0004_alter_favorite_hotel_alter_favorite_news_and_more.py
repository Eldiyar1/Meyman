# Generated by Django 4.2.3 on 2023-07-17 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0003_travelservice_price_alter_travelservice_service_name'),
        ('users', '0003_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='hotel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Hotel', to='travel.news'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='news',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='News', to='travel.news'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='travel_service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Travel_service', to='travel.travelservice'),
        ),
    ]
