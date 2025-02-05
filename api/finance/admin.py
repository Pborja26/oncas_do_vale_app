from django.contrib import admin
from finance import models as finance_models
from utils.admin import BaseModelAdmin
# Register your models here.
@admin.register(finance_models.Balance)
class BalanceAdmin(BaseModelAdmin):
  list_display = ('id', 'name', 'description', 'value', 'created_by')
  search_fields = ['id', 'name']

@admin.register(finance_models.FlowType)
class FlowTypeAdmin(BaseModelAdmin):
  list_display = ('id', 'name', 'flow_type')
  list_filter = ['flow_type']
  search_fields = ['id', 'name']

@admin.register(finance_models.CashFlow)
class CashFlowAdmin(BaseModelAdmin):
  list_display = ('id', 'user', 'flow_type', 'value', 'balance')
  list_filter = ['flow_type']
  search_fields = ['id', 'user', 'value', 'balance']
