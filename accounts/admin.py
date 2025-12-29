# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff')
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = UserAdmin.add_fieldsets

admin.site.register(CustomUser, CustomUserAdmin)