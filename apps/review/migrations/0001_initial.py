# Generated by Django 4.2.3 on 2023-08-08 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.PositiveIntegerField(blank=True, choices=[(1, ' ✭ '), (2, ' ✭  ✭ '), (3, ' ✭  ✭  ✭ '), (4, ' ✭  ✭  ✭  ✭ '), (5, ' ✭  ✭  ✭  ✭  ✭ ')], default=0, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
