from django.contrib import admin
from transactions.models import Transactions


class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('number', 'user', 'provider', 'status', 'amount', 'create_at', 'props')
    search_fields = ['number']
    list_filter = ('create_at', 'status', 'provider')

admin.site.register(Transactions, TransactionsAdmin)
