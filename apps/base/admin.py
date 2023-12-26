from django.contrib import admin
# Register your models here.
# my imports
from apps.base import models

class PhoneSettingInline(admin.TabularInline):
    model=models.SettingPhone
    extra=1

class SettingFilterAdmin(admin.ModelAdmin):
    list_filter=('instagram',)
    list_display=('instagram',)
    search_fields=('instagram',)
    inlines=[PhoneSettingInline]

admin.site.register(models.Setting, SettingFilterAdmin)
# 
class SettingFilterAdmin(admin.ModelAdmin):
    list_filter=('compani1',)
    list_display=('compani1',)
    search_fields=('compani1',)
admin.site.register(models.Menu)
admin.site.register(models.Logo)

class AboutFilterAdmin(admin.ModelAdmin):
    list_filter=('descriptions',)
    list_display=('descriptions',)
    search_fields=('descriptions',)
admin.site.register(models.About, AboutFilterAdmin)

class BlogFilterAdmin(admin.ModelAdmin):
    list_filter=('descriptions_1',)
    list_display=('descriptions_1',)
    search_fields=('descriptions_1',)
admin.site.register(models.Blog, BlogFilterAdmin)

class InfoPlusFilterAdmin(admin.ModelAdmin):
    list_filter=('descriptions_1',)
    list_display=('descriptions_1',)
    search_fields=('descriptions_1',)
admin.site.register(models.InfoPlus, InfoPlusFilterAdmin)

class ChoiceFilterAdmin(admin.ModelAdmin):
    list_filter=('titlle', )
    list_display=('titlle', )
    search_fields=('titlle', )
admin.site.register(models.Choice, ChoiceFilterAdmin)