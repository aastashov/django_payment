from django.contrib import admin
from models import Chat, Message, ClimeProvider


class AdminMessage(admin.TabularInline):
    model = Message


class AdminChat(admin.ModelAdmin):
    list_display = ('title', 'status', 'provider')
    inlines = [AdminMessage]


class AdminClimeProvider(admin.ModelAdmin):
    list_display = ('provider', 'email', 'name', 'phone_number')

admin.site.register(Chat, AdminChat)
admin.site.register(ClimeProvider, AdminClimeProvider)
