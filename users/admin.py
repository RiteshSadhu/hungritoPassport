# users/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name = 'Profile'
    verbose_name_plural = 'Profiles'
    readonly_fields = ('created_at', 'updated_at')


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_filter = ('is_active', 'is_staff', 'date_joined')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('username', 'whatsapp_number', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'whatsapp_number', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'username', 'whatsapp_number')
    ordering = ('email',)
    inlines = [ProfileInline]

    readonly_fields = ('date_joined', 'last_login')
    list_display = ('email', 'username', 'whatsapp_number', 'is_active', 'date_joined', 'last_login')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)