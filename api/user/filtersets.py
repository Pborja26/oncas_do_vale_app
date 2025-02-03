from django_filters import rest_framework as filters
from user import models as user_models

class GroupFilterSet(filters.FilterSet):
  id = filters.NumberFilter(field_name="id")
  name = filters.CharFilter(field_name="name", lookup_expr="icontains")

class UserFilterSet(filters.FilterSet):
  id = filters.NumberFilter(field_name="id")
  name = filters.CharFilter(field_name="name", lookup_expr="icontains")

  class Meta:
    model = user_models.User
    fields = ['name', 'username', 'email']

class AthleteFilterSet(filters.FilterSet):
  id = filters.NumberFilter(field_name="id")
  category = filters.CharFilter(field_name="category", lookup_expr="icontains")

  class Meta:
    model = user_models.Athlete
    fields = ['user', 'nickname']