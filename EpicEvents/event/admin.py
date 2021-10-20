from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('client', 'event_date', 'event_status')
    search_fields = ('client',)
    list_filter = ('support_contact', 'client')
