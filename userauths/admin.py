from django.contrib import admin
from .models import User, Profile
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    search_fields = ['full_name', 'username']
    list_display = ['username', 'full_name', 'gender', 'email']

class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['full_name', 'user__username']
    list_display = ['full_name', 'user__username', 'verified']

admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
