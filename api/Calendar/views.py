from django.shortcuts import render
from rest_framework import viewsets
from Calendar import models as calendarmodels
from Calendar import serializers as calendarserializers
# Create your views here.
class EventTypeViewSet(viewsets.ModelViewSet):
  queryset = calendarmodels.EventType.objects.all()
  serializer_class = calendarserializers.EventTypeSerializer

class EventViewSet(viewsets.ModelViewSet):
  queryset = calendarmodels.Event.objects.all()
  serializer_class = calendarserializers.EventSerializer

class EventPresenceViewSet(viewsets.ModelViewSet):
  queryset = calendarmodels.EventPresence.objects.all()
  serializer_class = calendarserializers.EventPresenceSerializer

