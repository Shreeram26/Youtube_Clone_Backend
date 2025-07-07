from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['get_username', 'email', 'is_verified']

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Username'

admin.site.register(Profile, ProfileAdmin)
