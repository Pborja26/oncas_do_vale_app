from django.shortcuts import render
from utils.views import BaseViewSet
from agenda import models as agenda_models
from agenda import filtersets as agenda_filters
from agenda import serializers as agenda_serializers
# Create your views here.
class EventTypeViewSet(BaseViewSet):
  queryset = agenda_models.EventType.objects.all()
  filterset_class = agenda_filters.EventTypeFilterSet
  serializer_class = agenda_serializers.EventTypeSerializer

class EventViewSet(BaseViewSet):
  queryset = agenda_models.Event.objects.all()
  filterset_class = agenda_filters.EventFilterSet
  serializer_class = agenda_serializers.EventSerializer

class EventPresence(BaseViewSet):
  queryset = agenda_models.EventPresence.objects.all()
  filterset_class = agenda_filters.EventPresenceFilterSet
  serializer_class = agenda_serializers.EventPresenceSerializer
