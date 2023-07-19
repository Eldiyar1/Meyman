from django.db import models

class Author(models.Model):
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    fullname = models.CharField(
        max_length=100,
        verbose_name="ФИО автора"
    )

    def __str__(self):
        return self.fullname


class News(models.Model):
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    title = models.CharField(max_length=255, verbose_name="Заголовок")
    image = models.ImageField(upload_to='images/news', verbose_name='Картинка новости', blank=True, null=True)
    content = models.TextField(verbose_name="Содержание")
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="news", verbose_name='Автор')
    published_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    link = models.URLField(max_length=200, blank=True, null=True, verbose_name="Ссылка на источник")

    def __str__(self):
        return self.title

    def author_fullname_list(self):
        return [self.author.fullname]

    def formatted_published_date(self):
        return self.published_date.strftime('%d-%m-%Y')