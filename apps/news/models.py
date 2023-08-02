from django.db import models

class News(models.Model):
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    title = models.CharField(max_length=255, verbose_name="Заголовок")
    image = models.ImageField(upload_to='images/news', verbose_name='Изображение новости', blank=True, null=True)
    content = models.TextField(verbose_name="Содержание")
    published_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    link = models.URLField(max_length=200, blank=True, null=True, verbose_name="Ссылка на источник")
    is_favorite = models.BooleanField(null=True, blank=True, default=False, verbose_name='Добавить в избраное')

    def __str__(self):
        return self.title