from django.contrib import admin
from payments.models import Providers, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'display', 'img')


class ProvidersAdmin(admin.ModelAdmin):
    list_display = ('name', 'account', 'category', 'display', 'img')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Providers, ProvidersAdmin)
