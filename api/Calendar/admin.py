from django.contrib import admin
from Calendar import models as CalendarModels
# Register your models here.
@admin.register(CalendarModels.EventType)
class EventTypeAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'description', 'created_in', 'updated_in')
  list_filter = ['name']
  search_fields = ['id', 'name']

@admin.register(CalendarModels.Event)
class EventAdmin(admin.ModelAdmin):
  list_display = ('event', 'init_date', 'start_time', 'end_date', 'end_time')
  list_filter = ['visibility']

@admin.register(CalendarModels.EventPresence)
class EventPresenceAdmin(admin.ModelAdmin):
  list_display = ('id', 'event', 'user', 'presence_confirmation')