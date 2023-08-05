# Generated by Django 4.2.3 on 2023-08-05 17:04

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0019_housing_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(choices=[('1_bedroom_double', 'Двухместный номер с 1 кроватью'), ('2_bedroom_twin', 'Двухместный с 2 отдельными кроватями'), ('1_or_2_bedroom', 'Двухместный номер с 1 кроватью или 2 отдельными кроватями'), ('luxury', 'Люкс'), ('3_bedroom', 'Трехместный номер'), ('family', 'Семейный'), ('deluxe', 'Делюкс'), ('4_bedroom', 'Четырехместный'), ('penthouse', 'Пентхаус'), ('connecting', 'Коннектирующийся номер'), ('business', 'Бизнес'), ('royal_luxury', 'Королевский люкс'), ('economy', 'Эконом'), ('standard', 'Стандартный')], max_length=50, verbose_name='название номера')),
                ('price_per_night', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='цена за ночь')),
                ('room_amenities', multiselectfield.db.fields.MultiSelectField(choices=[('air_conditioner', 'Кондиционер'), ('hair_dryer', 'Фен'), ('washing_machine', 'Стиральная машина'), ('iron', 'Утюг'), ('dryer', 'Сушильная машина'), ('fridge', 'Холодильник'), ('tv', 'Телевизор'), ('microwave', 'Микроволновка'), ('heating', 'Отопление'), ('sofa_bed', 'Диван-кровать'), ('folding_bed', 'Раскладная кровать'), ('Double bed', 'Двуспальная кровать'), ('wardrobe', 'Шкаф или гардероб'), ('linen', 'Белье'), ('clothes_hanger', 'Вешалка для одежды'), ('complimentary_toiletries', 'Бесплатные туалетно-косметические принадлежности'), ('toilet_paper', 'Туалетная бумага'), ('kitchen_utensils', 'Кухонные принадлежности'), ('electric_kettle', 'Электрический чайник'), ('city_view', 'Вид на город'), ('garden_view', 'Вид на сад'), ('high_toilet', 'Высокий туалет'), ('toilet_with_handles', 'Туалет с поручнями'), ('accessible_to_disabled_guests', 'Подходит для гостей с ограниченными возможностями'), ('work_desk', 'Рабочий стол'), ('room_cleaning', 'Уборка'), ('coffee_teapot', 'Кофеварка/чайник'), ('cable_satellite_tv', 'Кабельное / спутниковое телевидение'), ('bidet', 'Биде'), ('connecting_rooms_available', 'Доступны смежные номера'), ('room_service', 'Обслуживание номеров'), ('safe', 'Безопасный'), ('sitting_area', 'Зона отдыха'), ('telephone', 'Телефон'), ('bottled_water', 'Бутилированная вода'), ('Safe', 'Сейф'), ('laptop_safe_box', 'Сейф для ноутбука'), ('private_bathroom', 'Частные ванные комнаты'), ('wake_up_service', 'Услуга будильник / будильник'), ('minibar', 'Минибар'), ('flat_screen_tv', 'Телевизор с плоским экраном'), ('bath_or_shower', 'Ванна/душ'), ('Dressers', 'Комоды'), ('Mini kitchen', 'Мини кухня'), ('Fireplace', 'Камин'), ('Appetizers', 'Закуски'), ('2 rooms', '2 комнаты')], max_length=100, verbose_name='Удобства номера')),
                ('num_rooms', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1, verbose_name='Количество комнат в номере')),
                ('bedrooms', models.CharField(choices=[('1 bedroom', '1 спальня'), ('2 bedrooms', '2 спальни'), ('More than 3 bedrooms', 'Больше 3 спален')], max_length=50, verbose_name='Количество спален')),
                ('bed_type', models.CharField(choices=[('Single', 'Отдельные'), ('Double', 'Двуспальная'), ('Kingsize', 'Kingsize'), ('Queensize', 'Queensize'), ('Диван-кровать', 'Диван-кровать')], max_length=50, verbose_name='Тип кроватей')),
                ('single_bed_count', models.PositiveIntegerField(default=0, verbose_name='Количество односпальных кроватей')),
                ('double_bed_count', models.PositiveIntegerField(default=0, verbose_name='Количество двуспальных кроватей')),
                ('queen_bed_count', models.PositiveIntegerField(default=0, verbose_name='Количество широких (queen-size) кроватей')),
                ('king_bed_count', models.PositiveIntegerField(default=0, verbose_name='Количество широких (king-size) кроватей')),
                ('sofa_bed_count', models.PositiveIntegerField(default=0, verbose_name='Количество диван-кроватей')),
                ('max_guest_capacity', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)], verbose_name='Максимальная вместимость гостей в номере')),
                ('room_area', models.PositiveIntegerField(verbose_name='Площадь комнаты(м²)')),
                ('smoking_allowed', models.BooleanField(default=False, verbose_name='Разрешено ли курение в комнате')),
                ('without_card', models.BooleanField(choices=[(True, 'Да'), (False, 'Нет')], default=True, verbose_name='Без банковской карты')),
                ('free_cancellation', models.BooleanField(choices=[(True, 'Да'), (False, 'Нет')], default=False, verbose_name='Бесплатная отмена')),
                ('payment', models.CharField(choices=[('Pay now', 'К оплате сейчас'), ('Prepayment', 'Предоплата'), ('Cash payment', 'Оплата наличными')], default='К оплате сейчас', max_length=50, verbose_name='Оплата')),
                ('policy', models.CharField(choices=[('before_00_00_on_check_in_day', 'До 00:00 в день заезда'), ('anytime', 'В любое время')], max_length=50, verbose_name='Правила бесплатной отмены')),
            ],
            options={
                'verbose_name': 'Номер',
                'verbose_name_plural': 'Номера',
            },
        ),
        migrations.RemoveField(
            model_name='housing',
            name='bed_type',
        ),
        migrations.RemoveField(
            model_name='housing',
            name='bedrooms',
        ),
        migrations.RemoveField(
            model_name='housing',
            name='double_bed_count',
        ),
        migrations.RemoveField(
            model_name='housing',
            name='free_cancellation',
        ),
        migrations.RemoveField(
            model_name='housing',
            name='image',
        ),
        migrations.RemoveField(
            model_name='housing',
            name='king_bed_count',
        ),
        migrations.RemoveField(
            model_name='housing',
            name='max_guest_capacity',
        ),
        migrations.RemoveField(
            model_name='housing',
            name='num_rooms',
        ),
        migrations.RemoveField(
            model_name='housing',
            name='payment',
        ),
        migrations.RemoveField(
            model_name='housing',
            name='policy',
        ),
        migrations.RemoveField(
            model_name='housing',
            name='price_per_night',
        ),
        migrations.RemoveField(
            model_name='housing',
            name='queen_bed_count',
        ),
        migrations.RemoveField(
            model_name='housing',
            name='room_amenities',
        ),
        migrations.RemoveField(
            model_name='housing',
            name='room_area',
        ),
        migrations.RemoveField(
            model_name='housing',
            name='room_name',
        ),
        migrations.RemoveField(
            model_name='housing',
            name='single_bed_count',
        ),
        migrations.RemoveField(
            model_name='housing',
            name='smoking_allowed',
        ),
        migrations.RemoveField(
            model_name='housing',
            name='sofa_bed_count',
        ),
        migrations.RemoveField(
            model_name='housing',
            name='without_card',
        ),
        migrations.CreateModel(
            name='RoomImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='images/rooms/', verbose_name='Изображение номера')),
                ('housing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_images', to='travel.room')),
            ],
            options={
                'verbose_name': 'Изображение места жительства',
                'verbose_name_plural': 'Изображения места жительства',
            },
        ),
        migrations.AddField(
            model_name='room',
            name='housing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='travel.housing'),
        ),
    ]
