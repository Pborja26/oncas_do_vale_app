from rest_framework import serializers
from Finance import models as financemodels

class FlowTypeSerializer(serializers.ModelSerializer):
  class Meta: 
    model = financemodels.FlowType
    fields = '__all__'

class BalanceSerializer(serializers.ModelSerializer):
  class Meta:
    model = financemodels.Balance
    fields = '__all__'

class CashFlowSerializer(serializers.ModelSerializer):
  class Meta:
    model = financemodels.CashFlow
    fields = '__all__'