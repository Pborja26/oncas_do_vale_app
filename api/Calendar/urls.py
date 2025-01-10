from rest_framework import routers
from Calendar import views

router = routers.SimpleRouter(trailing_slash=False)

router.register("event_type", views.EventTypeViewSet, basename="EventType")
router.register("event", views.EventViewSet, basename="Event")
router.register("event_presence", views.EventPresenceViewSet, basename="EventPresence")

urlpatterns = [
    *router.urls
]
