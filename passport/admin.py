from django.contrib import admin
from .models import Profile


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'nationality', 'phone_number', 'city', 'country')
    search_fields = ('user__username', 'nationality', 'phone_number', 'city', 'country')
    list_filter = ('nationality', 'country')