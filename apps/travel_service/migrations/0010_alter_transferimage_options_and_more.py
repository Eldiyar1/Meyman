# Generated by Django 4.2.3 on 2023-08-10 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_service', '0009_rename_roomimage_transferimage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transferimage',
            options={'verbose_name': 'Изображение трансфера', 'verbose_name_plural': 'Изображения трансферов'},
        ),
        migrations.RemoveField(
            model_name='transfer',
            name='passenger_capacity',
        ),
        migrations.RemoveField(
            model_name='transfer',
            name='transfer_image',
        ),
        migrations.AddField(
            model_name='transfer',
            name='passenger_sits',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20)], default=1, verbose_name='Пассажирских мест'),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='brand',
            field=models.CharField(choices=[('Мерседес-бенц', 'Мерседес-бенц'), ('Лендровер', 'Лендровер'), ('БМВ', 'БМВ'), ('Вольво', 'Вольво'), ('Шевролед', 'Шевролед'), ('Фольксваген', 'Фольксваген'), ('Хонда', 'Хонда'), ('Ауди', 'Ауди'), ('Хендай', 'Хендай'), ('Форд', 'Форд'), ('Киа', 'Киа'), ('Лексус', 'Лексус'), ('Мицубиси', 'Мицубиси'), ('Рено', 'Рено'), ('Опель', 'Опель'), ('Субару', 'Субару'), ('Мазда', 'Мазда'), ('Порше', 'Порше'), ('Дэу', 'Дэу'), ('Лада', 'Лада'), ('Сузуки', 'Сузуки'), ('Инфинити', 'Инфинити'), ('Ссанг Йонг', 'Ссанг Йонг'), ('Ниссан', 'Ниссан'), ('Тойота', 'Тойота')], max_length=50, verbose_name='Марка трансфера'),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='category',
            field=models.CharField(choices=[('Легковушка', 'Легковушка'), ('Минивэн', 'Минивэн'), ('Внедорожник', 'Внедорожник'), ('Автобус', 'Автобус'), ('Кроссовер', 'Кроссовер')], max_length=50, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='color',
            field=models.CharField(choices=[('Серебристый', 'Серебристый'), ('Черный', 'Черный'), ('Белый', 'Белый'), ('Серый', 'Серый'), ('Бежевый', 'Бежевый'), ('Бирюзовый', 'Бирюзовый'), ('Бордовый', 'Бордовый'), ('Бронза', 'Бронза'), ('Хамелеон', 'Хамелеон'), ('Жёлтый', 'Жёлтый'), ('Зеленый', 'Зеленый'), ('Золотой', 'Золотой'), ('Коричневый', 'Коричневый'), ('Фиолетовый', 'Фиолетовый'), ('Синий', 'Синий'), ('Красный', 'Красный'), ('Оранжевый', 'Оранжевый'), ('Розовый', 'Розовый'), ('Сиреневый', 'Сиреневый'), ('Вишня', 'Вишня'), ('Баклажан', 'Баклажан'), ('Голубой', 'Голубой')], max_length=50, verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]
