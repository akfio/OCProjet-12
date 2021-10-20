from rest_framework import viewsets
from .models import Event
from client.models import Client
from .serializers import EventSerializer
from EpicEvents.permissions import IsSale, IsSupport, IsManagement

from user.models import CustomUser


class AllEventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    permission_classes = [IsSale | IsSupport | IsManagement]
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_queryset(self):
        events = self.queryset.filter(client=self.kwargs["client_pk"])
        return events

    def perform_create(self, serializer_class):
        client = Client.objects.get(id=self.kwargs["client_pk"])
        contact = self.request.user
        if contact.type == CustomUser.SALE:
            serializer_class.save(client=client)

"""
    def get_permissions(self):
        # if self.request.user ==j
            #return
       # elif self.request.user == support
            #return
"""
