from django.contrib import admin
from .models import trips, categories


class TripsAdmin(admin.ModelAdmin):
    list_display = (
        'venue',
        'rec_owner',
        'location',
        'locale',
        'categories',
        'day',
        'spaces',
        'rating',
    )


class CategoriesAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(trips, TripsAdmin)
admin.site.register(categories, CategoriesAdmin)
