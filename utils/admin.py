from django.contrib import admin

# Register your models here.
class BaseInfoModelAdmin(admin.ModelAdmin):
    readonly_fields = ("created_by", "updated_by")
    def save_model(self, request, obj, form, change):
        obj.save(user=request.user)