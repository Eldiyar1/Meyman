from django.contrib import admin
from .models import News, Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['fullname']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'formatted_published_date']
    list_filter = ['published_date']
    search_fields = ['title', 'author__username']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['published_date']
        return []
