# Generated by Django 4.2.3 on 2023-09-10 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0010_alter_housingreservation_check_in_date_and_more'),
        ('advertising', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertising',
            name='image',
        ),
        migrations.RemoveField(
            model_name='advertising',
            name='link',
        ),
        migrations.RemoveField(
            model_name='advertising',
            name='text',
        ),
        migrations.RemoveField(
            model_name='advertising',
            name='title',
        ),
        migrations.AddField(
            model_name='advertising',
            name='added',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='advertising',
            name='housing',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='travel.housing', verbose_name='Место жительства'),
            preserve_default=False,
        ),
    ]
