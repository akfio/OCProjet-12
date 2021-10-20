from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from django.urls import path, include
from .views import EventViewSet, AllEventViewSet
from client.urls import router as client

app_name = 'event'

event_router = routers.NestedSimpleRouter(client, r'clients', lookup='client')
event_router.register(r'events', EventViewSet, basename="event")

all_events_router = DefaultRouter()
all_events_router.register(r'AllEvents', AllEventViewSet, basename='AllEvent')

urlpatterns = [
    path('', include(event_router.urls)),
    path('', include(all_events_router.urls))
]