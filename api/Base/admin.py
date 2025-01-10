from django.contrib import admin
from Base import models
# Register your models here.
@admin.register(models.themeType)
class ThemeTypeAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'description', 'created_in', 'updated_in')

@admin.register(models.theme)
class ThemeAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'color', 'theme_type', 'created_in', 'updated_in')
