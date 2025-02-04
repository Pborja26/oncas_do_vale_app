from django.contrib import admin

# Register your models here.
class BaseModelAdmin(admin.ModelAdmin):
  readonly_fields = ['created_by', 'updated_by']

  def save_model(self, request, obj, form, change):
    """Define automaticamente created_by e updated_by ao salvar no Django Admin"""
    if not obj.pk:
        obj.created_by = request.user
    obj.updated_by = request.user
    super().save_model(request, obj, form, change)