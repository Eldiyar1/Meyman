# Generated by Django 4.2.3 on 2023-08-05 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0023_rename_housing_roomimage_room_alter_roomimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='images/rooms/', verbose_name='Изображение номера'),
        ),
    ]
