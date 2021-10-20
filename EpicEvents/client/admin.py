from django.contrib import admin
from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('company', 'first_name', 'last_name')
    search_fields = ('company',)
    list_filter = ('sales_contact',)
