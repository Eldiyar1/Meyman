from django.contrib import admin

from .models import Profile, AdminReview

admin.site.register(AdminReview)
admin.site.register(Profile)
