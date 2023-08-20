from django.contrib import admin
from .models import Store, Ages, GenderType, Category, BoxType


@admin.register(Store)
class StoreDecor(admin.ModelAdmin):
    list_display = ("user", "name", "code", "category", "gender", "age", "available")
    prepopulated_fields = {
        'slug': ["name", "brand", "code"]
    }
    list_filter = ("name", "category", "gender", "age", "available")
    search_fields = ("name", "category", "gender", "age", "available")


@admin.register(Ages)
class AgeDecor(admin.ModelAdmin):
    list_display = ("age", )


@admin.register(GenderType)
class GenderDecor(admin.ModelAdmin):
    list_display = ("name", )


@admin.register(Category)
class CategoryDecor(admin.ModelAdmin):
    list_display = ("name", )


@admin.register(BoxType)
class CategoryDecor(admin.ModelAdmin):
    list_display = ("name", )
