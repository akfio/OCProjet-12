from rest_framework import viewsets

from .models import Contract
from .serializers import ContractSerializer
from client.models import Client
from EpicEvents.permissions import IsSale, IsManagement
from user.models import CustomUser


class AllContractViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


class ContractViewSet(viewsets.ModelViewSet):
    permission_classes = [IsSale | IsManagement]
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

    def get_queryset(self):
        contracts = self.queryset.filter(client=self.kwargs["client_pk"])
        return contracts

    def perform_create(self, serializer_class):
        client = Client.objects.get(id=self.kwargs["client_pk"])
        contact = self.request.user
        if contact.type == CustomUser.SALE:
            serializer_class.save(sales_contact=contact, client=client)