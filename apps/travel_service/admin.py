from django.contrib import admin
from .models import Transfer, TransferReservation


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ('brand', 'year', 'fuel_consumption')
    list_filter = ('brand', 'year', 'fuel_consumption')
    search_fields = ('brand', 'year')


@admin.register(TransferReservation)
class TransferReservationAdmin(admin.ModelAdmin):
    list_display = (
        'destination_location', 'transfer_location', 'pickup_date', 'pickup_time', 'return_location', 'return_date',
        'return_time', 'with_driver')
    list_filter = ('transfer_location', 'destination_location', 'pickup_date', 'return_location', 'return_date',
                   'different_pickup_places')
    search_fields = ('transfer_location',)
