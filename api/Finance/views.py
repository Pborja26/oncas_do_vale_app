from django.shortcuts import render
from rest_framework import viewsets
from Finance import models as financemodels
from Finance import serializers as financeserializers
# Create your views here.
class FlowTypeViewSet(viewsets.ModelViewSet):
  queryset = financemodels.FlowType.objects.all()
  serializer_class = financeserializers.FlowTypeSerializer

class BalanceViewSet(viewsets.ModelViewSet):
  queryset = financemodels.Balance.objects.all()
  serializer_class = financeserializers.BalanceSerializer

class CashFlowViewSet(viewsets.ModelViewSet):
  queryset = financemodels.CashFlow.objects.all()
  serializer_class = financeserializers.CashFlowSerializer