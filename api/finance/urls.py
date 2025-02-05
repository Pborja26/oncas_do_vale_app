from rest_framework import routers
from finance import views as finance_views

router = routers.SimpleRouter(trailing_slash=False)

router.register("balance/", finance_views.BalanceViewSet, basename="Balance")
router.register("flow_type/", finance_views.FlowTypeViewSet, basename="Flow_type")
router.register("cash_flow/", finance_views.CashFlowViewSet, basename="Cash_flow")

urlpatterns = [
    *router.urls
]
