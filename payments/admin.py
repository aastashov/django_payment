from django.contrib import admin
from payments.models import Providers, Category

admin.site.register(Providers)
admin.site.register(Category)
