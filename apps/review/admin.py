from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['comment', 'stars', 'date_added']
