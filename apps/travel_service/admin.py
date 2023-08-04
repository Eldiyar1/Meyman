from django.contrib import admin
from .models import Transfer, TransferReservation, TransferImage


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ('brand', 'category', 'body_type', 'transmission', 'passenger', 'fuel_consumption',  'year')
    list_filter = ('brand', 'category', 'body_type', 'transmission', 'passenger', 'fuel_consumption', 'year')
    search_fields = ('brand', 'year')


@admin.register(TransferImage)
class TransferImageAdmin(admin.ModelAdmin):
    list_display = ('image',)


@admin.register(TransferReservation)
class TransferReservationAdmin(admin.ModelAdmin):
    list_display = (
        'destination_location', 'transfer_location', 'pickup_date', 'pickup_time', 'return_location', 'return_date',
        'return_time', 'with_driver')
    list_filter = ('transfer_location', 'destination_location', 'pickup_date', 'return_location', 'return_date',
                   'different_pickup_places')
    search_fields = ('transfer_location',)
