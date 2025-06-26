from django_filters import rest_framework as filters
from user import models as user_models

class GroupFilterSet(filters.FilterSet):
    class Meta:
        model = user_models.Group
        fields = ["id", "name"]

class UserFilterSet(filters.FilterSet):
    class Meta:
        model = user_models.User
        fields = ["id", "name"]

class AthleteFilterSet(filters.FilterSet):

    class Meta:
        model = user_models.Athlete
        fields = ["id"]
