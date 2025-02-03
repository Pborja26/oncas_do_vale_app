from django.contrib import admin
from utils.admin import BaseModelAdmin
from user import models as user_models
# Register your models here.
@admin.register(user_models.Group)
class GroupAdmin(BaseModelAdmin):
  list_display = ('id', 'name', 'description', 'created_by', 'created_in', 'updated_by', 'updated_in')
  filter_horizontal = ['permissions']

@admin.register(user_models.User)
class UserAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'group', 'username', 'email', 'birth_date')

@admin.register(user_models.Athlete)
class AthleteAdmin(BaseModelAdmin):
  list_display = ('id', 'user', 'nickname', 'category')
