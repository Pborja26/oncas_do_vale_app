from rest_framework import routers
from Material import views

router = routers.SimpleRouter(trailing_slash=False)

router.register("condition", views.ConditionViewSet, basename='Condition')
router.register("material_type", views.MaterialTypeViewSet, basename='MaterialType')
router.register("material", views.MaterialViewSet, basename='Material')
router.register("product", views.ProductViewSet, basename='Product')

urlpatterns = [
    *router.urls
]
