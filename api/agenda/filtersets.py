from django_filters import rest_framework as filters
from agenda import models as agenda_models

class EventTypeFilterSet(filters.FilterSet):
  id = filters.NumberFilter(field_name="id")
  name = filters.CharFilter(field_name="name", lookup_expr="icontains")

class EventFilterSet(filters.FilterSet):
  id = filters.NumberFilter(field_name="id")
  name = filters.CharFilter(field_name="name", lookup_expr="icontains")

class EventPresenceFilterSet(filters.FilterSet):
  id = filters.NumberFilter(field_name="id")
  event_id = filters.NumberFilter(field_name="event_id")
  user = filters.CharFilter(field_name="user", lookup_expr="icontains")
