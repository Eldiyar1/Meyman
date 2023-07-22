from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

from django.core.validators import MinValueValidator, MaxValueValidator


class Housing(models.Model):
    HOUSING_CHOICES = (
        ('Отели', 'Отели'),
        ('Хостелы', 'Хостелы'),
        ('Апартаменты', 'Апартаменты'),
        ('Гостевые дома', 'Гостевые дома'),
        ('Санатории', 'Санатории'),
    )

    ACCOMMODATION_CHOICES = (
        ("Жилье целиком", "Жилье целиком"),
        ("Комната", "Комната"),
        ("Общая комната", "Общая комната"),
    )

    BED_CHOICES = (
        ("Отдельные", "Отдельные"),
        ("Двуспальная", "Двуспальная"),
        ("Больше 3х", "Больше 3х"),
        ("Kingsize", "Kingsize"),
        ("Queensize ", "Queensize "),
    )

    FOOD_CHOICES = (
        ("Все включено", "Все включено"),
        ("Завтрак включен", "Завтрак включен"),
        ("Не включено", "Не включено"),
        ("С собственной кухней", "С собственной кухней"),
    )

    housing_name = models.CharField(max_length=255, verbose_name="Название места жительства")
    image = models.ImageField(upload_to='media/housing/', verbose_name="Изображение места жительства")
    description = models.TextField(verbose_name="Описание места жительства")
    min_and_max_price_per_night = models.DecimalField(max_digits=10, decimal_places=2,
                                                      validators=[MinValueValidator(10),
                                                                  MaxValueValidator(500)], verbose_name="цена за ночь")
    bathrooms = models.PositiveIntegerField(verbose_name='Количество ванн', default=1)
    beds = models.PositiveIntegerField(verbose_name='Количество кроватей', default=1)
    location = models.CharField(max_length=255, verbose_name="местоположение жилища")
    housing_type = models.CharField(max_length=255, choices=HOUSING_CHOICES, verbose_name="Тип жилья")
    accommodation_type = models.CharField(max_length=255, choices=ACCOMMODATION_CHOICES, verbose_name="Тип размещения")
    bed_type = models.CharField(max_length=255, choices=BED_CHOICES, verbose_name="Тип кроватей")
    food_type = models.CharField(max_length=50, choices=FOOD_CHOICES, default="Не включено", verbose_name="Тип питания")

    class Meta:
        verbose_name = "Жильё"
        verbose_name_plural = "Жильё"

    def __str__(self):
        return self.housing_name


class Hotel(Housing):
    class Meta:
        verbose_name = "Отель"
        verbose_name_plural = "Отели"


class Hostel(Housing):
    class Meta:
        verbose_name = "Хостел"
        verbose_name_plural = "Хостелы"


class Apartment(Housing):
    class Meta:
        verbose_name = "Апартаменты"
        verbose_name_plural = "Апартаменты"


class GuestHouse(Housing):
    class Meta:
        verbose_name = "Гостиница"
        verbose_name_plural = "Гостиницы"


class Sanatorium(Housing):
    class Meta:
        verbose_name = "Санаторий"
        verbose_name_plural = "Санатории"





class HousingAmenities(models.Model):
    housing = models.OneToOneField(Housing, on_delete=models.CASCADE, related_name='housing_amenities')
    free_internet = models.BooleanField(default=False, verbose_name='Бесплатный интернет')
    spa_services = models.BooleanField(default=False, verbose_name="Спа услуги")
    parking = models.BooleanField(default=False, verbose_name="Парковка")
    bar_or_restaurant = models.BooleanField(default=False, verbose_name="Бар/Ресторан")
    pool = models.BooleanField(default=False, verbose_name="Бассейн")
    airport_transfer = models.BooleanField(default=False, verbose_name='Трансфер от/до аэропорта')
    fitness = models.BooleanField(default=False, verbose_name="Фитнес")
    pet_allowed = models.BooleanField(default=False, verbose_name="Можно с питомцами")
    indoor_pool = models.BooleanField(default=False, verbose_name="Крытый бассейн")
    non_smoking_rooms = models.BooleanField(default=False, verbose_name='Номера для некурящих')
    wifi = models.BooleanField(default=False, verbose_name='Wifi')
    room_service = models.BooleanField(default=False, verbose_name='Доставка еды и напитков в номер')
    coffee_teapot = models.BooleanField(default=False, verbose_name='Кофеварка/чайник')
    bar = models.BooleanField(default=False, verbose_name='Бар')

    garden_furniture = models.BooleanField(default=False, verbose_name='Садовая мебель')
    sun_terrace = models.BooleanField(default=False, verbose_name='Терасса для загара')
    garden = models.BooleanField(default=False, verbose_name='Сад')
    wine_champagne = models.BooleanField(default=False, verbose_name='Вино/шампанское (платно)')
    kids_menu = models.BooleanField(default=False, verbose_name='Детское меню (платно)')
    breakfast_in_room = models.BooleanField(default=False, verbose_name='Завтрак в номер')
    restaurant = models.BooleanField(default=False, verbose_name='Archa Restaurant')
    free_wifi = models.BooleanField(default=False, verbose_name='Бесплатный Wi-Fi на территории всего отеля')
    daily_cleaning = models.BooleanField(default=False, verbose_name='Ежедневная уборка')
    laundry_service = models.BooleanField(default=False, verbose_name='Услуги по глажению одежды (платно)')
    paid_cleaning = models.BooleanField(default=False, verbose_name='Химчистка (платно)')
    paid_laundry = models.BooleanField(default=False, verbose_name='Прачечная (платно)')
    fax_xerox = models.BooleanField(default=False, verbose_name='Факс/ксерокопирование (платно)')
    conference_banquet_hall = models.BooleanField(default=False, verbose_name='Конференц-зал/банкетный зал (платно)')
    fire_extinguishers = models.BooleanField(default=False, verbose_name='Огнетушители')
    smoke_detectors = models.BooleanField(default=False, verbose_name='Датчики дыма')
    outdoor_surveillance = models.BooleanField(default=False, verbose_name='Видеонаблюдения снаружи здания')
    public_areas_surveillance = models.BooleanField(default=False,
                                                    verbose_name='Видеонаблюдения в местах общего пользования')
    security_alarm = models.BooleanField(default=False, verbose_name='Охранная сигнализация')
    full_time_security = models.BooleanField(default=False, verbose_name='Круглосуточная охрана')
    safe = models.BooleanField(default=False, verbose_name='Сейф')

    invoices_issued = models.BooleanField(default=False, verbose_name='Выдаются счета')
    lockers = models.BooleanField(default=False, verbose_name="Запирающиеся шкафчики")
    concierge_service = models.BooleanField(default=False, verbose_name='Услуги консьержа')
    atm_on_site = models.BooleanField(default=False, verbose_name='Банкомат на территории отеля')
    luggage_storage = models.BooleanField(default=False, verbose_name='Хранение багажа')
    express_check_in = models.BooleanField(default=False, verbose_name='Ускоренная регистрация')
    full_time_front_desk = models.BooleanField(default=False, verbose_name='Круглосуточная стойка регистрации')

    indoor_pool_heated = models.BooleanField(default=False, verbose_name='Крытый бассейн/бассейн с подогревом')
    transfer_paid = models.BooleanField(default=False, verbose_name='Трансфер (платно)')
    food_delivery_to_room_paid = models.BooleanField(default=False,
                                                     verbose_name='Доставка продуктов питания в номер (платно)')
    smoking_areas = models.BooleanField(default=False, verbose_name='Места для курения')
    air_conditioner = models.BooleanField(default=False, verbose_name='Кондиционер')
    heating = models.BooleanField(default=False, verbose_name='Отопление')
    car_rental = models.BooleanField(default=False, verbose_name='Прокат автомобилей')
    packed_lunches = models.BooleanField(default=False, verbose_name='Упакованные ланчи')
    ironing_facilities = models.BooleanField(default=False, verbose_name='Гладильные принадлежности')
    buffet_breakfast = models.BooleanField(default=False, verbose_name='Завтрак "шведский стол"')
    free_instant_coffee = models.BooleanField(default=False, verbose_name='Бесплатный растворимый кофе')
    free_tea = models.BooleanField(default=False, verbose_name='Бесплатный чай')
    happy_hour = models.BooleanField(default=False, verbose_name='Счастливый час')
    special_diet_menu = models.BooleanField(default=False, verbose_name='Специальное диетическое меню')
    taxi_service = models.BooleanField(default=False, verbose_name='Служба такси')
    internet_business_center = models.BooleanField(default=False, verbose_name='Бизнес-центр с доступом в Интернет')
    facial_treatments = models.BooleanField(default=False, verbose_name='Процедуры для лица')
    foot_massage = models.BooleanField(default=False, verbose_name='Массаж ног')
    full_body_massage = models.BooleanField(default=False, verbose_name='Массаж всего тела')
    hammam = models.BooleanField(default=False, verbose_name='Хаммам')
    manual_massage = models.BooleanField(default=False, verbose_name='Ручной массаж')
    head_massage = models.BooleanField(default=False, verbose_name='Массаж головы')
    massage = models.BooleanField(default=False, verbose_name='Массаж')
    neck_massage = models.BooleanField(default=False, verbose_name='Массаж шеи')
    steam_room = models.BooleanField(default=False, verbose_name='Паровая комната')
    currency_exchange = models.BooleanField(default=False, verbose_name='Обмен валюты')
    bell_staff_porter = models.BooleanField(default=False, verbose_name='Швейцар')
    individual_check_in_check_out = models.BooleanField(default=False,
                                                        verbose_name='Индивидуальная регистрация заезда/отъезда')
    dry_cleaning = models.BooleanField(default=False, verbose_name='Сухая чистка')
    shoe_shine = models.BooleanField(default=False, verbose_name='Чистка обуви')

    class Meta:
        verbose_name = "Удобства в объекте"
        verbose_name_plural = "Удобства в объекте"


class RoomAmenities(models.Model):
    housing = models.OneToOneField(Housing, on_delete=models.CASCADE, related_name='room_amenities')
    air_conditioner = models.BooleanField(default=False, verbose_name="Кондиционер")
    hair_dryer = models.BooleanField(default=False, verbose_name="Фен")
    washing_machine = models.BooleanField(default=False, verbose_name="Стиральная машина")
    iron = models.BooleanField(default=False, verbose_name="Утюг")
    dryer = models.BooleanField(default=False, verbose_name="Сушильная машина")
    fridge = models.BooleanField(default=False, verbose_name="Холодильник")
    tv = models.BooleanField(default=False, verbose_name="Телевизор")
    microwave = models.BooleanField(default=False, verbose_name="Микроволновка")
    heating = models.BooleanField(default=False, verbose_name="Отопление")
    sofa_bed = models.BooleanField(default=False, verbose_name='Диван-кровать')
    folding_bed = models.BooleanField(default=False, verbose_name='Раскладная кровать')
    wardrobe = models.BooleanField(default=False, verbose_name='Шкаф или гардероб')
    linen = models.BooleanField(default=False, verbose_name='Белье')
    clothes_hanger = models.BooleanField(default=False, verbose_name='Вешалка для одежды')
    complimentary_toiletries = models.BooleanField(default=False,
                                                   verbose_name='Бесплатные туалетно-косметические принадлежности')
    toilet_paper = models.BooleanField(default=False, verbose_name='Туалетная бумага')
    kitchen_utensils = models.BooleanField(default=False, verbose_name='Кухонные принадлежности')
    electric_kettle = models.BooleanField(default=False, verbose_name='Электрический чайник')
    city_view = models.BooleanField(default=False, verbose_name='Вид на город')
    garden_view = models.BooleanField(default=False, verbose_name='Вид на сад')
    high_toilet = models.BooleanField(default=False, verbose_name='Высокий туалет')
    toilet_with_handles = models.BooleanField(default=False, verbose_name='Туалет с поручнями')
    accessible_to_disabled_guests = models.BooleanField(default=False,
                                                        verbose_name='Подходит для гостей с ограниченными возможностями')
    work_desk = models.BooleanField(default=False, verbose_name="Рабочий стол")
    room_cleaning = models.BooleanField(default=False, verbose_name="Уборка")
    coffee_teapot = models.BooleanField(default=False, verbose_name="Кофеварка/чайник")
    cable_satellite_tv = models.BooleanField(default=False, verbose_name="Кабельное / спутниковое телевидение")
    bidet = models.BooleanField(default=False, verbose_name="Биде")
    connecting_rooms_available = models.BooleanField(default=False, verbose_name="Доступны смежные номера")
    room_service = models.BooleanField(default=False, verbose_name="Обслуживание номеров")
    safe = models.BooleanField(default=False, verbose_name="Безопасный")
    sitting_area = models.BooleanField(default=False, verbose_name="Зона отдыха")
    telephone = models.BooleanField(default=False, verbose_name="Телефон")
    bottled_water = models.BooleanField(default=False, verbose_name="Бутилированная вода")
    laptop_safe_box = models.BooleanField(default=False, verbose_name="Сейф для ноутбука")
    private_bathroom = models.BooleanField(default=False, verbose_name="Частные ванные комнаты")
    wake_up_service = models.BooleanField(default=False, verbose_name="Услуга будильник / будильник")
    minibar = models.BooleanField(default=False, verbose_name="Минибар")
    flat_screen_tv = models.BooleanField(default=False, verbose_name="Телевизор с плоским экраном")
    bath_or_shower = models.BooleanField(default=False, verbose_name="Ванна/душ")

    class Meta:
        verbose_name = "Удобства в номере"
        verbose_name_plural = "Удобства в номере"
