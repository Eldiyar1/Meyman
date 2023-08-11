# Generated by Django 4.2.3 on 2023-08-10 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0018_remove_room_double_bed_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housing',
            name='parking',
            field=models.CharField(choices=[('Да, бесплатно', 'Да, бесплатно'), ('Да, платно', 'Да, платно'), ('Нет', 'Нет')], default='Нет', max_length=50, verbose_name='Услуги парковки'),
        ),
    ]
