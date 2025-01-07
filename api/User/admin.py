from django.contrib import admin
from User import models as UserModels
# Register your models here.
@admin.register(UserModels.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_in', 'updated_in')
    search_fields = ['name']

@admin.register(UserModels.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'username', 'password', 'group', 'email', 'created_in', 'updated_in')
    list_filter = ['group']
    search_fields = ['id', 'name']

@admin.register(UserModels.Athlete)
class AthleteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'category', 'id_document', 'birth_date', 'blood_type', 'created_in', 'updated_in')
    list_filter = ['category']
    search_fields = ['user', 'id', 'id_document']