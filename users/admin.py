from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Device


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'phone_number', 'full_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'date_joined')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'full_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'phone_number', 'full_name', 'is_active', 'is_staff')}
        ),
    )
    search_fields = ('username', 'email', 'phone_number', 'full_name')
    ordering = ('username',)


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('user', 'device_id', 'name', 'last_login', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at', 'last_login')
    search_fields = ('user__username', 'device_id', 'name')
    readonly_fields = ('created_at', 'last_login')


admin.site.register(User, CustomUserAdmin)
admin.site.register(Device, DeviceAdmin)