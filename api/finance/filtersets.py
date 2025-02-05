from django_filters import rest_framework as filters

class BalanceFilterSet(filters.FilterSet):
  id = filters.NumberFilter(field_name="id")
  name = filters.CharFilter(field_name="name", lookup_expr="icontains")
  description = filters.CharFilter(field_name="description", lookup_expr="icontains")


class FlowTypeFilterSet(filters.FilterSet):
  id = filters.NumberFilter(field_name="id")
  name = filters.CharFilter(field_name="name", lookup_expr="icontains")
  flow_type = filters.CharFilter(field_name="flow_type", lookup_expr="iexact")

class CashFlowFilterSet(filters.FilterSet):
  id = filters.NumberFilter(field_name="id")
  user = filters.CharFilter(field_name="user", lookup_expr="icontains")
  flow_type = filters.CharFilter(field_name="flow_type", lookup_expr="icontains")
  balance = filters.CharFilter(field_name="balance", lookup_expr="icontains")
