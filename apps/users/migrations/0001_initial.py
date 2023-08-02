# Generated by Django 4.2.3 on 2023-08-02 07:30

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('travel', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('travel_service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=45)),
                ('user_type', models.CharField(choices=[('client', 'Client'), ('owner', 'Owner')], max_length=10)),
                ('date_of_birth', models.DateField(null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AdminReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/', verbose_name='Profiles_avatar')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='Email')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, verbose_name='Номер телефона')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CarReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in_date', models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 8, 2))], verbose_name='дата бронирование')),
                ('check_out_date', models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 8, 2))])),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_service.transfer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AccommodationReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in_date', models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 8, 2))], verbose_name='Заезд')),
                ('check_out_date', models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 8, 2))], verbose_name='Выезд')),
                ('booking_type', models.CharField(choices=[('Без банковской карты', 'Без банковской карты'), ('Бесплатная отмена', 'Бесплатная отмена')], default='Без банковской карты', max_length=50, verbose_name='Бронирование')),
                ('payment_type', models.CharField(choices=[('К оплате сейчас', 'К оплате сейчас'), ('Предоплата', 'Предоплата'), ('Оплата наличными', 'Оплата наличными')], default='К оплате сейчас', max_length=50, verbose_name='Оплата')),
                ('accommodation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.housing')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]