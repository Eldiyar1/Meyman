import datetime
from django.db import migrations, models
from django.core.validators import MinValueValidator

class Migration(migrations.Migration):

    dependencies = [
        ('travel_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='check_in_date',
            field=models.DateField(validators=[MinValueValidator(datetime.date(2023, 7, 27))], verbose_name='Заезд'),
        ),
        migrations.AlterField(
            model_name='search',
            name='check_out_date',
            field=models.DateField(validators=[MinValueValidator(datetime.date(2023, 7, 27))], verbose_name='Выезд'),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='pickup_date',
            field=models.DateField(validators=[MinValueValidator(datetime.date(2023, 7, 27))], verbose_name='Дата получения трансфера'),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='return_date',
            field=models.DateField(validators=[MinValueValidator(datetime.date(2023, 7, 27))], verbose_name='Дата возврата трансфера'),
        ),
    ]