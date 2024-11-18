from django.contrib import admin
from .models import Contact


class contactAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name', 
        'email',
        'comments',
        'date',
    )

admin.site.register(Contact, contactAdmin)


