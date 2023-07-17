from django.contrib import admin
from .models import TravelService, Hotel, News, Author, Signal

admin.site.register(TravelService)
admin.site.register(Hotel)
admin.site.register(News)
admin.site.register(Author)
admin.site.register(Signal)