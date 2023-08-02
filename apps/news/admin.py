from django.contrib import admin
from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'author_fullname', 'published_date']
    list_filter = ['published_date']
    search_fields = ['title', 'author_fullname']
