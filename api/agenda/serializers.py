from rest_framework import serializers
from agenda import models as agenda_models

class EventTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = agenda_models.EventType
    fields = "__all__"

class EventSerializer(serializers.ModelSerializer):
  class Meta:
    model = agenda_models.Event
    fields = "__all__"

class EventPresenceSerializer(serializers.ModelSerializer):
  class Meta:
    model = agenda_models.EventPresence
    fields = "__all__"
