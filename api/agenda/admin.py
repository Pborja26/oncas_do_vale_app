from django.contrib import admin
from utils.admin import BaseModelAdmin
from agenda import models as agenda_models
# Register your models here.
@admin.register(agenda_models.EventType)
class EventTypeAdmin(BaseModelAdmin):
  list_display = ('id', 'name', 'description', 'created_by')


@admin.register(agenda_models.Event)
class EventAdmin(BaseModelAdmin):
  list_display = ('id', 'name', 'event_type', 'init_date', 'end_date')
  list_filter = ['visibility']

@admin.register(agenda_models.EventPresence)
class EventPresenceAdmin(BaseModelAdmin):
  list_display = ('id', 'event_id', 'user')
