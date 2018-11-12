from datetime import date
from decimal import Decimal
from typing import List

from django.test import TestCase

import moneyed

from .models import ExchangeRate
from .scraper import ExchangeRateScraper, ExchangeRate as ExchangeRateData
from .tasks import scrape_exchange_rates


class DummyExchangeRateScraper(ExchangeRateScraper):

    def get_exchange_rates(self) -> List[ExchangeRateData]:
        return [
            ExchangeRateData(
                source_currency=moneyed.PLN,
                target_currency=moneyed.EUR,
                rate=Decimal('4.20'),
                date=date(2018, 1, 1),
            ),
            ExchangeRateData(
                source_currency=moneyed.HUF,
                target_currency=moneyed.EUR,
                rate=Decimal('44.20'),
                date=date(2018, 1, 1),
            ),
            ExchangeRateData(
                source_currency=moneyed.HUF,
                target_currency=moneyed.EUR,
                rate=Decimal('44.20'),
                date=date(2018, 1, 1),
            ),
        ]


exchange_rate_scraper = DummyExchangeRateScraper()


class ExchangeRateScraperTest(TestCase):

    def test_scrap_exchange_rate(self):
        scrape_exchange_rates(exchange_rate_scraper)

        model = ExchangeRate.objects.get(source_currency=moneyed.PLN)
        
        assert ExchangeRate.objects.count() == 2
        assert model.source_currency == moneyed.PLN.code
        assert model.target_currency == moneyed.EUR.code
        assert model.rate == Decimal('4.20')
        assert model.date == date(2018, 1, 1)
