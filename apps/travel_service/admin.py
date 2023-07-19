from django.contrib import admin
from .models import TravelService


@admin.register(TravelService)
class TravelServiceAdmin(admin.ModelAdmin):
    list_display = ['service_name', 'price', 'location', 'start_date', 'end_date', 'is_available']
    list_filter = ['is_available', 'start_date', 'end_date']
    search_fields = ['service_name']
