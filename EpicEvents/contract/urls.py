from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from django.urls import path, include
from .views import ContractViewSet, AllContractViewSet
from client.urls import router as client

app_name = 'contract'

contract_router = routers.NestedSimpleRouter(client, r'clients', lookup='client')
contract_router.register(r'contracts', ContractViewSet, basename="contract")

all_contracts_router = DefaultRouter()
all_contracts_router.register(r'AllContracts', AllContractViewSet, basename='AllContract')

urlpatterns = [
    path('', include(contract_router.urls)),
    path('', include(all_contracts_router.urls))
]