from django.shortcuts import render
from finance import models as finance_models
from finance import filtersets as finance_filters
from finance import serializers as finance_serializers
from utils.views import BaseViewSet
# Create your views here.

class BalanceViewSet(BaseViewSet):
  queryset = finance_models.Balance.objects.all()
  filterset_class = finance_filters.BalanceFilterSet
  serializer_class = finance_serializers.BalanceSerializer

class FlowTypeViewSet(BaseViewSet):
  queryset = finance_models.FlowType.objects.all()
  filterset_class = finance_filters.FlowTypeFilterSet
  serializer_class = finance_serializers.FlowTypeSerializer

class CashFlowViewSet(BaseViewSet):
  queryset = finance_models.CashFlow.objects.all()
  filterset_class = finance_filters.CashFlowFilterSet
  serializer_class = finance_serializers.CashFlowSerializer
