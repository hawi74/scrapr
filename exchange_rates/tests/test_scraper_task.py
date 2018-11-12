from datetime import datetime
from decimal import Decimal
from typing import List

from django.test import TestCase

import moneyed
import pytz

from ..models import ExchangeRate
from ..scraper import ExchangeRateScraper, ExchangeRate as ExchangeRateData
from ..tasks import scrape_exchange_rates


class DummyExchangeRateScraper(ExchangeRateScraper):

    def get_exchange_rates(self) -> List[ExchangeRateData]:
        return [
            ExchangeRateData(
                source_currency=moneyed.PLN,
                target_currency=moneyed.EUR,
                rate=Decimal('4.20'),
                datetime=datetime(2018, 1, 1, 1, 1, 1, tzinfo=pytz.UTC),
            ),
            ExchangeRateData(
                source_currency=moneyed.HUF,
                target_currency=moneyed.EUR,
                rate=Decimal('44.20'),
                datetime=datetime(2018, 1, 1, 1, 1, 1, tzinfo=pytz.UTC),
            ),
            ExchangeRateData(
                source_currency=moneyed.HUF,
                target_currency=moneyed.EUR,
                rate=Decimal('44.20'),
                datetime=datetime(2018, 1, 1, 1, 1, 1, tzinfo=pytz.UTC),
            ),
        ]


exchange_rate_scraper = DummyExchangeRateScraper()


class ExchangeRateScraperTest(TestCase):

    def test_scrape_exchange_rate_saves_correct_data(self):
        scrape_exchange_rates(exchange_rate_scraper)

        model = ExchangeRate.objects.get(source_currency=moneyed.PLN)
        
        assert model.source_currency == moneyed.PLN.code
        assert model.target_currency == moneyed.EUR.code
        assert model.rate == Decimal('4.20')
        assert model.datetime == datetime(2018, 1, 1, 1, 1, 1, tzinfo=pytz.UTC)

    def test_scrape_exchange_rates_skips_existing_recods(self):
        scrape_exchange_rates(exchange_rate_scraper)

        assert ExchangeRate.objects.count() == 2
