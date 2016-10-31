from django.contrib import admin
from payments.models import Provider, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'display', 'img')


class ProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'account', 'category', 'display', 'img')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Provider, ProviderAdmin)
