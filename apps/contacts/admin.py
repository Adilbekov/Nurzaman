from django.contrib import admin

# Register your models here.
from apps.contacts import models

class ContactFilterAdmin(admin.ModelAdmin):
    list_filter=('name',)
    list_display=('name', 'phone')
    search_fields=('name', 'phone')
admin.site.register(models.Cotact, ContactFilterAdmin)