# Generated by Django 4.2.3 on 2023-08-10 15:37

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0009_rename_housereservation_housingreservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housing',
            name='accommodation_type',
            field=models.CharField(choices=[('Жилье целиком', 'Жилье целиком'), ('Комната', 'Комната'), ('Общая комната', 'Общая комната')], max_length=50, verbose_name='Тип размещения'),
        ),
        migrations.AlterField(
            model_name='housing',
            name='breakfast_type',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Азиатский', 'Азиатский'), ('Континентальный', 'Континентальный'), ('Шведский', 'Шведский')], max_length=100, null=True, verbose_name='Какой тип завтрака вы предлагаете?'),
        ),
        migrations.AlterField(
            model_name='housing',
            name='food_type',
            field=models.CharField(choices=[('Все включено', 'Все включено'), ('Завтрак включен', 'Завтрак включен'), ('Не включено', 'Не включено'), ('С собственной кухней', 'С собственной кухней')], default='Не включено', max_length=50, verbose_name='Тип питания'),
        ),
        migrations.AlterField(
            model_name='housing',
            name='housing_amenities',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Бесплатный интернет', 'Бесплатный интернет'), ('Спа услуги', 'Спа услуги'), ('Ресторан', 'Ресторан'), ('Спортивный зал', 'Спортивный зал'), ('Бассейн', 'Бассейн'), ('Трансфер от/до аэропорта', 'Трансфер от/до аэропорта'), ('Фитнес', 'Фитнес'), ('Крытый бассейн', 'Крытый бассейн'), ('Номера для некурящих', 'Номера для некурящих'), ('Wifi', 'Wifi'), ('Доставка еды и напитков в номер', 'Доставка еды и напитков в номер'), ('Кофеварка/чайник', 'Кофеварка/чайник'), ('Бар', 'Бар'), ('Садовая мебель', 'Садовая мебель'), ('Терасса для загара', 'Терасса для загара'), ('Сад', 'Сад'), ('Вино/шампанское (платно)', 'Вино/шампанское (платно)'), ('Детское меню (платно)', 'Детское меню (платно)'), ('Завтрак в номер', 'Завтрак в номер'), ('Завтрак включен в стоимость проживания?', 'Завтрак включен в стоимость проживания?'), ('Бесплатный Wi-Fi на территории всего отеля', 'Бесплатный Wi-Fi на территории всего отеля'), ('Ежедневная уборка', 'Ежедневная уборка'), ('Услуги по глажению одежды (платно)', 'Услуги по глажению одежды (платно)'), ('Химчистка (платно)', 'Химчистка (платно)'), ('Прачечная (платно)', 'Прачечная (платно)'), ('Факс/ксерокопирование (платно)', 'Факс/ксерокопирование (платно)'), ('Конференц-зал/банкетный зал (платно)', 'Конференц-зал/банкетный зал (платно)'), ('Огнетушители', 'Огнетушители'), ('Датчики дыма', 'Датчики дыма'), ('Видеонаблюдения снаружи здания', 'Видеонаблюдения снаружи здания'), ('Видеонаблюдения в местах общего пользования', 'Видеонаблюдения в местах общего пользования'), ('Охранная сигнализация', 'Охранная сигнализация'), ('Круглосуточная охрана', 'Круглосуточная охрана'), ('Сейф', 'Сейф'), ('Выдаются счета', 'Выдаются счета'), ('Запирающиеся шкафчики', 'Запирающиеся шкафчики'), ('Услуги консьержа', 'Услуги консьержа'), ('Банкомат на территории отеля', 'Банкомат на территории отеля'), ('Хранение багажа', 'Хранение багажа'), ('Ускоренная регистрация', 'Ускоренная регистрация'), ('Круглосуточная стойка регистрации', 'Круглосуточная стойка регистрации'), ('Трансфер (платно)', 'Трансфер (платно)'), ('Доставка продуктов питания в номер (платно)', 'Доставка продуктов питания в номер (платно)'), ('Места для курения', 'Места для курения'), ('Кондиционер', 'Кондиционер'), ('Отопление', 'Отопление'), ('Прокат автомобилей', 'Прокат автомобилей'), ('Упакованные ланчи', 'Упакованные ланчи'), ('Гладильные принадлежности', 'Гладильные принадлежности'), ('Завтрак "шведский стол"', 'Завтрак "шведский стол"'), ('Бесплатный растворимый кофе', 'Бесплатный растворимый кофе'), ('Бесплатный чай', 'Бесплатный чай'), ('Счастливый час', 'Счастливый час'), ('Специальное диетическое меню', 'Специальное диетическое меню'), ('Служба такси', 'Служба такси'), ('Бизнес-центр с доступом в Интернет', 'Бизнес-центр с доступом в Интернет'), ('Процедуры для лица', 'Процедуры для лица'), ('Массаж ног', 'Массаж ног'), ('Массаж всего тела', 'Массаж всего тела'), ('Хаммам', 'Хаммам'), ('Ручной массаж', 'Ручной массаж'), ('Массаж головы', 'Массаж головы'), ('Массаж', 'Массаж'), ('Массаж шеи', 'Массаж шеи'), ('Паровая комната', 'Паровая комната'), ('Обмен валюты', 'Обмен валюты'), ('Швейцар', 'Швейцар'), ('Индивидуальная регистрация заезда/отъезда', 'Индивидуальная регистрация заезда/отъезда'), ('Сухая чистка', 'Сухая чистка'), ('Чистка обуви', 'Чистка обуви'), ('Детская площадка', 'Детская площадка'), ('Можно c детьми', 'Можно c детьми'), ('C домашними животными', 'C домашними животными'), ('Берете ли вы плату за домашних животных?', 'Берете ли вы плату за домашних животных?'), ('Парковка', 'Парковка'), ('Джакузи', 'Джакузи'), ('Сауна', 'Сауна'), ('Камера хранения багажа', 'Камера хранения багажа'), ('Доступ людям с ограниченными возможностями', 'Доступ людям с ограниченными возможностями'), ('Сувенирный магазин', 'Сувенирный магазин'), ('Доступ в интернет: в номерах', 'Доступ в интернет: в номерах'), ('Доступ в интернет: на всей территории отеля', 'Доступ в интернет: на всей территории отеля'), ('Прокат автомобиля', 'Прокат автомобиля'), ('Питание', 'Питание'), ('Бар у бассейна', 'Бар у бассейна'), ('Кафе', 'Кафе')], max_length=1300, verbose_name='Удобства'),
        ),
        migrations.AlterField(
            model_name='housing',
            name='housing_type',
            field=models.CharField(choices=[('Отели', 'Отели'), ('Хостелы', 'Хостелы'), ('Квартиры', 'Квартиры'), ('Гостевые дома', 'Гостевые дома'), ('Санатории', 'Санатории')], max_length=50, verbose_name='Тип жилья'),
        ),
        migrations.AlterField(
            model_name='housing',
            name='parking',
            field=models.CharField(choices=[('Да, бесплатно', 'Да, бесплатно'), ('Да, платно', 'Да, платно'), ('Нет', 'Нет')], default='no', max_length=50, verbose_name='Услуги парковки'),
        ),
        migrations.AlterField(
            model_name='housing',
            name='parking_location',
            field=models.CharField(blank=True, choices=[('На территории', 'На территории'), ('За территорией', 'За территорией')], max_length=50, null=True, verbose_name='Местонахождение парковки'),
        ),
        migrations.AlterField(
            model_name='housing',
            name='region',
            field=models.CharField(choices=[('Бишкек', 'Бишкек'), ('Джалал-Абад', 'Джалал-Абад'), ('Иссык-Куль', 'Иссык-Куль'), ('Ош', 'Ош'), ('Нарын', 'Нарын'), ('Талас', 'Талас'), ('Баткен', 'Баткен')], max_length=50, verbose_name='Область'),
        ),
        migrations.AlterField(
            model_name='housingreservation',
            name='destination',
            field=models.CharField(choices=[('Бишкек', 'Бишкек'), ('Джалал-Абад', 'Джалал-Абад'), ('Иссык-Куль', 'Иссык-Куль'), ('Ош', 'Ош'), ('Нарын', 'Нарын'), ('Талас', 'Талас'), ('Баткен', 'Баткен')], max_length=100, verbose_name='Куда'),
        ),
        migrations.AlterField(
            model_name='room',
            name='bed_type',
            field=models.CharField(choices=[('Отдельные', 'Отдельные'), ('Двуспальная', 'Двуспальная'), ('Kingsize', 'Kingsize'), ('Queensize', 'Queensize'), ('Диван-кровать', 'Диван-кровать')], max_length=50, verbose_name='Тип кроватей'),
        ),
        migrations.AlterField(
            model_name='room',
            name='bedrooms',
            field=models.CharField(choices=[('1 спальня', '1 спальня'), ('2 спальни', '2 спальни'), ('Больше 3 спален', 'Больше 3 спален')], max_length=50, verbose_name='Количество спален'),
        ),
        migrations.AlterField(
            model_name='room',
            name='payment',
            field=models.CharField(choices=[('К оплате сейчас', 'К оплате сейчас'), ('Предоплата', 'Предоплата'), ('Оплата наличными', 'Оплата наличными')], default='К оплате сейчас', max_length=50, verbose_name='Оплата'),
        ),
        migrations.AlterField(
            model_name='room',
            name='policy',
            field=models.CharField(choices=[('До 00:00 в день заезда', 'До 00:00 в день заезда'), ('В любое время', 'В любое время')], max_length=50, verbose_name='Правила бесплатной отмены'),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_amenities',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Кондиционер', 'Кондиционер'), ('Фен', 'Фен'), ('Стиральная машина', 'Стиральная машина'), ('Утюг', 'Утюг'), ('Сушильная машина', 'Сушильная машина'), ('Холодильник', 'Холодильник'), ('Телевизор', 'Телевизор'), ('Микроволновка', 'Микроволновка'), ('Отопление', 'Отопление'), ('Диван-кровать', 'Диван-кровать'), ('Раскладная кровать', 'Раскладная кровать'), ('Двуспальная кровать', 'Двуспальная кровать'), ('Шкаф или гардероб', 'Шкаф или гардероб'), ('Белье', 'Белье'), ('Вешалка для одежды', 'Вешалка для одежды'), ('Бесплатные туалетно-косметические принадлежности', 'Бесплатные туалетно-косметические принадлежности'), ('Туалетная бумага', 'Туалетная бумага'), ('Кухонные принадлежности', 'Кухонные принадлежности'), ('Электрический чайник', 'Электрический чайник'), ('Вид на город', 'Вид на город'), ('Вид на сад', 'Вид на сад'), ('Высокий туалет', 'Высокий туалет'), ('Туалет с поручнями', 'Туалет с поручнями'), ('Подходит для гостей с ограниченными возможностями', 'Подходит для гостей с ограниченными возможностями'), ('Рабочий стол', 'Рабочий стол'), ('Уборка', 'Уборка'), ('Кофеварка/чайник', 'Кофеварка/чайник'), ('Кабельное / спутниковое телевидение', 'Кабельное / спутниковое телевидение'), ('Биде', 'Биде'), ('Доступны смежные номера', 'Доступны смежные номера'), ('Обслуживание номеров', 'Обслуживание номеров'), ('Безопасный', 'Безопасный'), ('Зона отдыха', 'Зона отдыха'), ('Телефон', 'Телефон'), ('Бутилированная вода', 'Бутилированная вода'), ('Сейф', 'Сейф'), ('Сейф для ноутбука', 'Сейф для ноутбука'), ('Частные ванные комнаты', 'Частные ванные комнаты'), ('Услуга будильник / будильник', 'Услуга будильник / будильник'), ('Минибар', 'Минибар'), ('Ванна/душ', 'Ванна/душ'), ('Комоды', 'Комоды'), ('Мини кухня', 'Мини кухня'), ('Камин', 'Камин'), ('Закуски', 'Закуски'), ('2 комнаты', '2 комнаты'), ('Тумба', 'Тумба'), ('Телевизор', 'Телевизор'), ('Ванная комната', 'Ванная комната'), ('Телефон', 'Телефон'), ('Комоды', 'Комоды'), ('Тапочки', 'Тапочки'), ('Халат', 'Халат')], max_length=700, verbose_name='Удобства'),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_name',
            field=models.CharField(choices=[('Двухместный номер с 1 кроватью', 'Двухместный номер с 1 кроватью'), ('Двухместный с 2 отдельными кроватями', 'Двухместный с 2 отдельными кроватями'), ('Двухместный номер с 1 кроватью или 2 отдельными кроватями', 'Двухместный номер с 1 кроватью или 2 отдельными кроватями'), ('Люкс', 'Люкс'), ('Трехместный номер', 'Трехместный номер'), ('Семейный', 'Семейный'), ('Делюкс', 'Делюкс'), ('Четырехместный', 'Четырехместный'), ('Пентхаус', 'Пентхаус'), ('Коннектирующийся номер', 'Коннектирующийся номер'), ('Бизнес', 'Бизнес'), ('Королевский люкс', 'Королевский люкс'), ('Эконом', 'Эконом'), ('Стандартный', 'Стандартный')], max_length=100, verbose_name='название номера'),
        ),
    ]
