from rest_framework import serializers
from finance import models as finance_models

class BalanceSerializer(serializers.ModelSerializer):
  class Meta:
    model = finance_models.Balance
    fields = "__all__"

class FlowTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = finance_models.FlowType
    fields = "__all__"

class CashFlowSerializer(serializers.ModelSerializer):
  class Meta:
    model = finance_models.CashFlow
    fields = "__all__"
