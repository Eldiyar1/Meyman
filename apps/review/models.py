from django.db import models

from apps.news.models import News
from apps.travel.models import Hotel
from apps.travel_service.models import Transfer


class Review(models.Model):

    CHOICES = (
        (1, " * "),
        (2, 2 * " * "),
        (3, 3 * " * "),
        (4, 4 * " * "),
        (5, 5 * " * "),
    )

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='review_news',
                             verbose_name='Новости',
                             null=True, blank=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='review_hotel',
                              verbose_name='Отели',
                              null=True, blank=True)
    transfer = models.ForeignKey(Transfer, on_delete=models.CASCADE,
                                       related_name='review_travel_service',
                                       verbose_name='Трэвел-услуги',
                                           null=True, blank=True)
    stars = models.PositiveIntegerField(default=0, blank=True, null=True, choices=CHOICES)
    comment = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")


    def str(self):
        return self.comment

    def formatted_date_added(self):
        return self.date_added.strftime('%d-%m-%Y')

