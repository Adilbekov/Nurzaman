from django.contrib import admin

# Register your models here.
from apps.secondary import models

class SlideFilterAdmin(admin.ModelAdmin):
    list_filter=('title',)
    list_display=('title',)
    search_fields=('title',)
admin.site.register(models.Slide, SlideFilterAdmin)
admin.site.register(models.Partners)

class InfoFilterAdmin(admin.ModelAdmin):
    list_filter=('descriptions',)
    list_display=('descriptions',)
    search_fields=('descriptions',)
admin.site.register(models.Info, InfoFilterAdmin)

class GellaryFilterAdmin(admin.ModelAdmin):
    list_filter=('descriptions','title')
    list_display=('descriptions','title')
    search_fields=('descriptions','title')
admin.site.register(models.ImageGallery, GellaryFilterAdmin)

class OneFilterAdmin(admin.ModelAdmin):
    list_filter=('descrioptions','title')
    list_display=('descrioptions','title')
    search_fields=('descrioptions','title')
admin.site.register(models.One, OneFilterAdmin)

class TwoFilterAdmin(admin.ModelAdmin):
    list_filter=('descriptions','title')
    list_display=('descriptions','title')
    search_fields=('descriptions','title')
admin.site.register(models.SlideTwo, TwoFilterAdmin)

class EnvironmentFilterAdmin(admin.ModelAdmin):
    list_filter=('descriptions_1','title')
    list_display=('descriptions_1','title')
    search_fields=('descriptions_1','title')
admin.site.register(models.Environment, EnvironmentFilterAdmin)

class StreetFilterAdmin(admin.ModelAdmin):
    list_filter=('name', 'description')
    list_display=('name', 'description')
    search_fields=('name', 'description')
admin.site.register(models.Street, StreetFilterAdmin)