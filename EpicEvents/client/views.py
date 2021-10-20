from rest_framework import viewsets
from EpicEvents.permissions import IsSale, IsManagement
from .models import Client
from .serializers import ClientSerializer
from user.models import CustomUser


class AllClientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientViewSet(viewsets.ModelViewSet):
    permission_classes = [IsSale | IsManagement]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get_queryset(self):
        client = self.queryset.filter(sales_contact=self.request.user)
        return client

    def perform_create(self, serializer_class):
        contact = self.request.user
        if contact.type == CustomUser.SALE:
            serializer_class.save(sales_contact=contact)