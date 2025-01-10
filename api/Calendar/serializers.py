from rest_framework import serializers
from Calendar import models as calendarmodels

class EventTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = calendarmodels.EventType
    fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
  class Meta:
    model = calendarmodels.Event
    fields = '__all__'

class EventPresenceSerializer(serializers.ModelSerializer):
  class Meta:
    model = calendarmodels.EventPresence
    fields = '__all__'
