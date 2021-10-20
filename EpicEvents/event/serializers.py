from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'client', 'event_date', 'attendees', 'event_status', 'support_contact', 'note')
