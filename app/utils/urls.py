from django.urls import path
from app.controllers.transaction_controller import create_transaction_view
from app.controllers.health_controller import health_check

urlpatterns = [
    path("transactions/", create_transaction_view),
    path("health/", health_check),
]