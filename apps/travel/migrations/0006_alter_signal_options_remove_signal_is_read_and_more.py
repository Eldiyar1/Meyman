# Generated by Django 4.2.3 on 2023-07-17 17:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travel', '0005_rename_notification_signal'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='signal',
            options={'verbose_name': 'Уведомление', 'verbose_name_plural': 'Уведомление'},
        ),
        migrations.RemoveField(
            model_name='signal',
            name='is_read',
        ),
        migrations.AddField(
            model_name='signal',
            name='s_read',
            field=models.BooleanField(default=False, verbose_name='Прочитанно'),
        ),
        migrations.AlterField(
            model_name='signal',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Когда написанно'),
        ),
        migrations.AlterField(
            model_name='signal',
            name='message',
            field=models.TextField(verbose_name='Сообщение'),
        ),
        migrations.AlterField(
            model_name='signal',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Кому'),
        ),
    ]
