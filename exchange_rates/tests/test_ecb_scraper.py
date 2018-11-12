from decimal import Decimal

from datetime import datetime, timezone, timedelta

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

        tzinfo = timezone(timedelta(seconds=3600))
        expected = [
            ExchangeRate(
                source_currency=moneyed.PLN,
                target_currency=moneyed.EUR,
                rate=Decimal('4.2968'),
                datetime=datetime(2018, 11, 12, 14, 15, tzinfo=tzinfo),
            ),
            ExchangeRate(
                source_currency=moneyed.PLN,
                target_currency=moneyed.EUR,
                rate=Decimal('4.2880'),
                datetime=datetime(2018, 11, 9, 14, 15, tzinfo=tzinfo),
            ),
            ExchangeRate(
                source_currency=moneyed.PLN,
                target_currency=moneyed.EUR,
                rate=Decimal('4.2915'),
                datetime=datetime(2018, 11, 8, 14, 15, tzinfo=tzinfo),
            ),
            ExchangeRate(
                source_currency=moneyed.PLN,
                target_currency=moneyed.EUR,
                rate=Decimal('4.2940'),
                datetime=datetime(2018, 11, 7, 14, 15, tzinfo=tzinfo),
            ),
            ExchangeRate(
                source_currency=moneyed.PLN,
                target_currency=moneyed.EUR,
                rate=Decimal('4.3088'),
                datetime=datetime(2018, 11, 6, 14, 15, tzinfo=tzinfo),
            ),
        ]

        assert result == expected
