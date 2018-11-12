from django.urls import path

from .views import ExchangeRateViewSet


urlpatterns = [
    path('', ExchangeRateViewSet.as_view()),
]
