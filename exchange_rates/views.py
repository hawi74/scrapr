from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from .filters import ExchangeRateFilterSet
from .models import ExchangeRate
from .serializers import ExchangeRateSerializer


class ExchangeRateViewSet(generics.ListAPIView):
    serializer_class = ExchangeRateSerializer
    queryset = ExchangeRate.objects.all()
    filter_backends = (
        DjangoFilterBackend,
    )
    filterset_class = ExchangeRateFilterSet
