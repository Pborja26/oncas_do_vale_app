from rest_framework import routers
from Base import views

router = routers.SimpleRouter(trailing_slash=False)

router.register("theme", views.ThemeView, basename="Theme")

urlpatterns = [
    *router.urls
]
