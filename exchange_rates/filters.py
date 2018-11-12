import django_filters

from .models import ExchangeRate


class ExchangeRateFilterSet(django_filters.FilterSet):
    datetime__gte = django_filters.DateTimeFilter(
        field_name='datetime',
        lookup_expr='gte',
    )
    datetime__lte = django_filters.DateTimeFilter(
        field_name='datetime',
        lookup_expr='lte',
    )

    class Meta:
        model = ExchangeRate
        fields = (
            'source_currency',
            'target_currency',
        )
