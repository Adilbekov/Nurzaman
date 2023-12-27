from django.contrib import admin

# Register your models here.
from apps.contacts import models

class ContactFilterAdmin(admin.ModelAdmin):
    list_filter=('name',)
    list_display=('name', 'phone')
    search_fields=('name', 'phone')
admin.site.register(models.Cotact, ContactFilterAdmin)

class Contact_2FilterAdmin(admin.ModelAdmin):
    list_filter=('name',)
    list_display=('name', 'phone')
    search_fields=('name', 'phone')
admin.site.register(models.Contact_2, Contact_2FilterAdmin)


class Contact_3FilterAdmin(admin.ModelAdmin):
    list_filter=('name',)
    list_display=('name', 'phone')
    search_fields=('name', 'phone')
admin.site.register(models.Contact_3, Contact_3FilterAdmin)