# Generated by Django 4.2.3 on 2023-08-10 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertising',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='ad_images/', verbose_name='Изображение')),
                ('link', models.URLField(verbose_name='Ссылка на рекламадателя')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True, verbose_name='человеко-понятный url')),
            ],
            options={
                'verbose_name': 'Реклама',
                'verbose_name_plural': 'Рекламы',
            },
        ),
    ]
