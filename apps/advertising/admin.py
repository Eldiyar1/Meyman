from django.contrib import admin
from .models import Advertising

# Register your models here.
@admin.register(Advertising)
class AdvertisingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title', )}

# admin.site.register(Advertising)