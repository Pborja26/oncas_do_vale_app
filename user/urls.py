from rest_framework import routers
from user import views

router = routers.SimpleRouter(trailing_slash=False)

router.register("group", views.GroupViewSet)
router.register("user", views.UserViewSet)
router.register("athlete", views.AthleteViewSet)

urlpatterns = [*router.urls]
