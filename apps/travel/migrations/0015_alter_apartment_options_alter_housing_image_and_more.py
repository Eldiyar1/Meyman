# Generated by Django 4.2.3 on 2023-08-10 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0014_alter_room_room_amenities'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apartment',
            options={'verbose_name': 'Квартира', 'verbose_name_plural': 'Квартиры'},
        ),
        migrations.AlterField(
            model_name='housing',
            name='image',
            field=models.ImageField(upload_to='housing', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_image',
            field=models.ImageField(upload_to='rooms', verbose_name='Изображение'),
        ),
    ]
