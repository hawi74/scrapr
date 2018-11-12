from rest_framework import generics

from .models import ExchangeRate
from .serializers import ExchangeRateSerializer


class ExchangeRateViewSet(generics.ListAPIView):
    serializer_class = ExchangeRateSerializer
    queryset = ExchangeRate.objects.all()
