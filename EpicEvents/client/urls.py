from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ClientViewSet, AllClientViewSet

app_name = 'client'

router = DefaultRouter()
router.register(r'clients', ClientViewSet, basename="client")

clients_router = DefaultRouter()
clients_router.register(r'AllClients', AllClientViewSet, basename="AllClient")


urlpatterns = [
    path('', include(router.urls)),
    path('', include(clients_router.urls))
]

