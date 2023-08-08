from django.contrib import admin
from .models import HouseFavorite

class HouseFavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'item')
    list_filter = ('user', 'item')
    search_fields = ('user__username', 'item__title')


@admin.register(HouseFavorite)
class HouseFavoriteAdmin(admin.ModelAdmin):
    fields = ('user', 'item')
