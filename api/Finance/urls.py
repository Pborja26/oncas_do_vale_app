from rest_framework import routers
from Finance import views

router = routers.SimpleRouter(trailing_slash=False)

router.register("flow_type", views.FlowTypeViewSet, basename="FlowType")
router.register("balance", views.BalanceViewSet, basename="Balance")
router.register("cash_flow", views.CashFlowViewSet, basename="CashFlow")

urlpatterns = [
    *router.urls
]
