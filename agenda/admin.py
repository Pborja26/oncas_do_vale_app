from django.contrib import admin
from agenda import models
from utils.admin import BaseInfoModelAdmin
# Register your models here.
@admin.register(models.EventType)
class EventTypeAdmin(BaseInfoModelAdmin):
    list_display = ["id", "name", "created_by", "updated_by"]

@admin.register(models.Event)
class EventAdmin(BaseInfoModelAdmin):
    list_display = ["id", "name", "date_init", "time_init"]