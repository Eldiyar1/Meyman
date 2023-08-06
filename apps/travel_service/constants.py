DESTINATION_CHOICES = (
    ('Bishkek', 'Бишкек'),
    ('Jalal-Abad', 'Джалал-Абад'),
    ('Issyk-Kul', 'Иссык-Куль'),
    ('Osh', 'Ош'),
    ('Naryn', 'Нарын'),
    ('Talas', 'Талас'),
    ('Batken', 'Баткен'),
)

CAR_CATEGORIES = (
    ('Car', 'Легковушка'),
    ('Minivan', 'Минивэн'),
    ('SUV', 'Внедорожник'),
    ('Bus', 'Автобус'),
    ('Crossover', 'Кроссовер'),
)

BRAND_CHOICES = (
    ('Mercedes-Benz', 'Мерседес-бенц'),
    ('Land Rover', 'Лендровер'),
    ('BMW', 'БМВ'),
    ('Volvo', 'Вольво'),
    ('Chevrolet', 'Шевролед'),
    ('Volkswagen', 'Фольксваген'),
    ('Honda', 'Хонда'),
    ('Audi', 'Ауди'),
    ('Hyundai', 'Хендай'),
    ('Ford', 'Форд'),
    ('Kia', 'Киа'),
    ('Lexus', 'Лексус'),
    ('Mitsubishi', 'Мицубиси'),
    ('Renault', 'Рено'),
    ('Opel', 'Опель'),
    ('Subaru', 'Субару'),
    ('Mazda', 'Мазда'),
    ('Porsche', 'Порше'),
    ('Daewoo', 'Дэу'),
    ('Lada', 'Лада'),
    ('Suzuki', 'Сузуки'),
    ('Infiniti', 'Инфинити'),
    ('SsangYong', 'Ссанг Йонг'),
    ('Nissan', 'Ниссан'),
    ('Toyota', 'Тойота'),
)

TRANSMISSION_TYPES = (
    ('Manual', 'Механическая'),
    ('Automatic', 'Автоматическая'),
    ('Other', 'Другое'),
)

STEERING_TYPES = (
    ('Left', 'Левый'),
    ('Right', 'Правый'),
)

BODY_TYPES = (
    ('Sedan', 'Седан'),
    ('Coupe', 'Купе'),
    ('Hatchback', 'Хэтчбек'),
    ('Liftback', 'Лифтбек'),
    ('Fastback', 'Фастбэк'),
    ('Wagon', 'Универсал'),
    ('Crossover', 'Кроссовер'),
    ('SUV', 'Внедорожник'),
    ('Passenger van', 'Легковой фургон'),
    ('Minivan', 'Минивэн'),
    ('Compact van', 'Компактвэн'),
    ('Microvan', 'Микровэн'),
    ('Convertible', 'Кабриолет'),
    ('Roadster', 'Родстер'),
    ('Targa', 'Тарга'),
    ('Landaulet', 'Ландо'),
    ('Limousine', 'Лимузин'),
)

DRIVE_TYPES = (
    ('Front', 'Передний'),
    ('Rear', 'Задний'),
    ('All-wheel', 'Полный'),
)

FUEL_TYPES = (
    ('Gasoline', 'Бензин'),
    ('Gasoline/Gas', 'Бензин/Газ'),
    ('Gas', 'Газ'),
    ('Diesel', 'Дизель'),
    ('Electric', 'Электрический'),
    ('Other', 'Другое'),
)

SEATING_CAPACITY = (
    ('2', '2 passengers'),
    ('5', '5 passengers'),
    ('8', '8 passengers'),
    ('Other', 'Other'),
)

CONDITION_CHOICES = (
    ('Good', 'Хорошее'),
    ('Excellent', 'Идеальное'),
    ('New', 'Новое'),
)

CURRENCY_CHOICES = (
    ('KGS', 'Сом (KGS)'),
    ('USD', 'Доллар (USD)'),
    ('EUR', 'Евро (EUR)'),
)

SAFETY_EQUIPMENT_CHOICES = [
    ('fire_extinguisher', 'Наличие огнетушителя'),
    ('first_aid_kit', 'Наличие аптечки'),
    ('spare_wheel', 'Наличие запасного колеса'),
    ('airbags', 'Наличие подушка безопасности'),
    ('emergency_tools', 'Наличие инструментов аварийной ситуации'),
    ('dashboard_camera', 'Наличие авторегистратора'),
]

COLOR_CHOICES = (
    ('Silver', 'Серебристый'),
    ('Black', 'Черный'),
    ('White', 'Белый'),
    ('Gray', 'Серый'),
    ('Beige', 'Бежевый'),
    ('Turquoise', 'Бирюзовый'),
    ('Burgundy', 'Бордовый'),
    ('Bronze', 'Бронза'),
    ('Chameleon', 'Хамелеон'),
    ('Yellow', 'Жёлтый'),
    ('Green', 'Зеленый'),
    ('Gold', 'Золотоый'),
    ('Brown', 'Коричневый'),
    ('Purple', 'Фиолетовый'),
    ('Blue', 'Синий'),
    ('Red', 'Красный'),
    ('Orange', 'Оранжевый'),
    ('Pink', 'Розовый'),
    ('Lilac', 'Сиреневый'),
    ('Cherry', 'Вишьня'),
    ('Eggplant', 'Баклажан'),
    ('Light blue', 'Голубой'),
)

AMENITIES_CHOICES = (
    ('Air conditioning', 'Кондиционер'),
    ('Parking sensor', 'Датчик парковки'),
    ('Heated seats and steering wheel', 'Подогрев сидений и руля'),
    ('Child seat', 'Детское кресло'),
)

PASSENGER_CAPACITY_CHOICES = [(i, i) for i in range(1, 21)]