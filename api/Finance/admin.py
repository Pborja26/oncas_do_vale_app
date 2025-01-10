from django.contrib import admin
from Finance import models as FinanceModels
# Register your models here.
@admin.register(FinanceModels.Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'balance', 'created_in', 'updated_in')

@admin.register(FinanceModels.FlowType)
class FlowTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'category', 'created_in', 'updated_in')
    list_filter = ['category']

@admin.register(FinanceModels.CashFlow)
class CashFlowAdmin(admin.ModelAdmin):
    list_display = ('id', 'flow_type', 'value', 'mov_date', 'balance')
    