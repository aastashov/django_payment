from django.contrib import admin
from profiles.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'phone', 'account')
    search_fields = ['account']

admin.site.register(Profile, ProfileAdmin)
