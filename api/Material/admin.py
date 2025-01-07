from django.contrib import admin
from Material import models as MaterialModels
# Register your models here.
@admin.register(MaterialModels.Condition)
class ConditionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'description', 'created_in', 'updated_in')
    search_fields = ['id', 'name', 'code']

@admin.register(MaterialModels.MaterialType)
class MaterialTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_in', 'updated_in')

@admin.register(MaterialModels.Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'material_type', 'condition', 'purchase_price', 'purchased_in')

@admin.register(MaterialModels.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'in_stock', 'production_price', 'profit_margin', 'selling_price')
    readonly_fields = ['selling_price']