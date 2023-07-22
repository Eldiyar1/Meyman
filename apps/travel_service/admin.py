from django.contrib import admin
from .models import Search, Transfer

@admin.register(Search)
class SearchAdmin(admin.ModelAdmin):
    list_display = ('destination', 'check_in_date', 'check_out_date', 'adults', 'teens', 'children', 'infants', 'pets')
    list_filter = ('destination', 'check_in_date', 'check_out_date')
    search_fields = ('region',)


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ('transfer_location', 'pickup_date', 'pickup_time', 'return_location', 'return_date', 'return_time', 'with_driver')
    list_filter = ('transfer_location', 'pickup_date', 'return_location', 'return_date')
    search_fields = ('transfer_location',)
