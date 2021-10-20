from django.contrib import admin
from .models import Contract, Status


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('client', 'status', 'amount')
    search_fields = ('client',)
    list_filter = ('sales_contact',)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('status',)
