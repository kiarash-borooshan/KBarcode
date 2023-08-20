from django.contrib import admin
from .models import Profile, EmProfile


@admin.register(Profile)
class ProfileDecore(admin.ModelAdmin):
    list_display = ("user", "phone_number")


@admin.register(EmProfile)
class EmProfileDecore(admin.ModelAdmin):
    list_display = ("user", "phone_number")
