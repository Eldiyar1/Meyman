# Generated by Django 4.2.3 on 2023-07-23 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0003_alter_housing_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='housing',
            name='bedrooms',
            field=models.PositiveIntegerField(choices=[(1, '1 спальня'), (2, '2 спальни'), (3, 'Больше 3 спален')], default=1, verbose_name='Количество спален'),
        ),
    ]
