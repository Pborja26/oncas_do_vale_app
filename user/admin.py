from django.contrib import admin
from user import models
from utils.admin import BaseInfoModelAdmin
# Register your models here.
@admin.register(models.Group)
class GroupAdmin(BaseInfoModelAdmin):
    list_display = ("id", "name", "created_by", "created_at", "updated_by", "updated_at")

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "group", "username", "email")
    search_fields = ("id", "name", "username")

@admin.register(models.Athlete)
class AthleteAdmin(BaseInfoModelAdmin):
    list_display = ("id", "user", "category")
    list_filter = ["category"]
