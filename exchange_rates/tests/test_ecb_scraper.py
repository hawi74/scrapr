from decimal import Decimal

from datetime import date

from django.test import TestCase

import moneyed

from ..scraper import ECBExchangeRateScraper, ExchangeRate


class ExchangeRateScraperTest(TestCase):

    def test_ecb_scraper(self):
        scraper = ECBExchangeRateScraper(
            source_currency=moneyed.PLN,
            target_currency=moneyed.EUR,
            data_source='exchange_rates/tests/assets/ecb_test_feed.html',
        )

        result = scraper.get_exchange_rates()

        expected = [
            ExchangeRate(
                source_currency=moneyed.PLN,
                target_currency=moneyed.EUR,
                rate=Decimal('4.2968'),
                date=date(2018, 11, 12),
            ),
            ExchangeRate(
                source_currency=moneyed.PLN,
                target_currency=moneyed.EUR,
                rate=Decimal('4.2880'),
                date=date(2018, 11, 9),
            ),
            ExchangeRate(
                source_currency=moneyed.PLN,
                target_currency=moneyed.EUR,
                rate=Decimal('4.2915'),
                date=date(2018, 11, 8),
            ),
            ExchangeRate(
                source_currency=moneyed.PLN,
                target_currency=moneyed.EUR,
                rate=Decimal('4.2940'),
                date=date(2018, 11, 7),
            ),
            ExchangeRate(
                source_currency=moneyed.PLN,
                target_currency=moneyed.EUR,
                rate=Decimal('4.3088'),
                date=date(2018, 11, 6),
            ),
        ]

        assert result == expected
