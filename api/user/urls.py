from rest_framework import routers
from user import views as user_views

router = routers.SimpleRouter(trailing_slash=False)

router.register("group/", user_views.GroupViewSet, basename="Group")
router.register("user/", user_views.UserViewSet, basename="User")
router.register("athlete/", user_views.AthleteViewSet, basename="Athlete")

urlpatterns = [
    *router.urls
]
