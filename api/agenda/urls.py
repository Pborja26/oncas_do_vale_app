from rest_framework import routers
from agenda import views as agenda_views

router = routers.SimpleRouter(trailing_slash=False)

router.register("event_type/", agenda_views.EventTypeViewSet, basename="EventType")
router.register("event/", agenda_views.EventViewSet, basename="Event")
router.register("event_presence/", agenda_views.EventPresence, basename="EventPresence")

urlpatterns = [
    *router.urls
]
