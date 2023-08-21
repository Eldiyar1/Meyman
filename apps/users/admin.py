from django.contrib import admin

from .models import Profile, CustomUser, ReviewSite

admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(ReviewSite)
