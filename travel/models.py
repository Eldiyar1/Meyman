from django.db import models


class Author(models.Model):
    fullname = models.CharField(max_length=150)

    def __str__(self):
        return self.fullname


class TravelService(models.Model):
    service_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.service_name


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=255)
    description = models.TextField()
    daily_price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    available_rooms = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.hotel_name


class News(models.Model):
    class Meta:
        verbose_name_plural = 'News'

    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='news')
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def author_fullname_list(self):
        return [self.author.fullname]
