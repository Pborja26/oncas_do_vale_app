from rest_framework import routers
from User import views

router = routers.SimpleRouter(trailing_slash=False)

router.register("group", views.GroupViewSet, basename="Group")
router.register("user", views.UserViewSet, basename="User")
router.register("athlete", views.AthleteViewSet, basename="Athlete")

urlpatterns = [
    *router.urls
]
