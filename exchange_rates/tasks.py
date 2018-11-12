from celery import shared_task

import moneyed

from .models import ExchangeRate
from .scraper import (
    ECBExchangeRateScraper,
    ExchangeRate as ExchangeRateData,
    ExchangeRateScraper,
)


def save_exchange_rate(exchange_rate: ExchangeRateData) -> None:
    if ExchangeRate.objects.filter(
        source_currency=exchange_rate.source_currency,
        target_currency=exchange_rate.target_currency,
        datetime=exchange_rate.datetime,
    ).exists():
        return

    model = ExchangeRate(
        source_currency=exchange_rate.source_currency,
        target_currency=exchange_rate.target_currency,
        rate=exchange_rate.rate,
        datetime=exchange_rate.datetime,
    )
    model.save()


def scrape_exchange_rates(scraper: ExchangeRateScraper) -> None:
    for exchange_rate in scraper.get_exchange_rates():
        save_exchange_rate(exchange_rate)


@shared_task
def scrape_all_exchange_rates():
    scrapers = [
        ECBExchangeRateScraper(
             source_currency=moneyed.USD,
             target_currency=moneyed.EUR,
             data_source='https://www.ecb.europa.eu/rss/fxref-usd.html',
        ),
        ECBExchangeRateScraper(
             source_currency=moneyed.JPY,
             target_currency=moneyed.EUR,
             data_source='https://www.ecb.europa.eu/rss/fxref-jpy.html',
        ),
        ECBExchangeRateScraper(
             source_currency=moneyed.BGN,
             target_currency=moneyed.EUR,
             data_source='https://www.ecb.europa.eu/rss/fxref-bgn.html',
        ),
        ECBExchangeRateScraper(
             source_currency=moneyed.CZK,
             target_currency=moneyed.EUR,
             data_source='https://www.ecb.europa.eu/rss/fxref-czk.html',
        ),
        ECBExchangeRateScraper(
             source_currency=moneyed.DKK,
             target_currency=moneyed.EUR,
             data_source='https://www.ecb.europa.eu/rss/fxref-dkk.html',
        ),
        ECBExchangeRateScraper(
             source_currency=moneyed.GBP,
             target_currency=moneyed.EUR,
             data_source='https://www.ecb.europa.eu/rss/fxref-gbp.html',
        ),
        ECBExchangeRateScraper(
             source_currency=moneyed.HUF,
             target_currency=moneyed.EUR,
             data_source='https://www.ecb.europa.eu/rss/fxref-huf.html',
        ),
        ECBExchangeRateScraper(
             source_currency=moneyed.PLN,
             target_currency=moneyed.EUR,
             data_source='https://www.ecb.europa.eu/rss/fxref-pln.html',
        ),
        ECBExchangeRateScraper(
             source_currency=moneyed.RON,
             target_currency=moneyed.EUR,
             data_source='https://www.ecb.europa.eu/rss/fxref-ron.html',
        ),
        ECBExchangeRateScraper(
             source_currency=moneyed.SEK,
             target_currency=moneyed.EUR,
             data_source='https://www.ecb.europa.eu/rss/fxref-sek.html',
        ),
        ECBExchangeRateScraper(
             source_currency=moneyed.CHF,
             target_currency=moneyed.EUR,
             data_source='https://www.ecb.europa.eu/rss/fxref-chf.html',
        ),
        ECBExchangeRateScraper(
             source_currency=moneyed.ISK,
             target_currency=moneyed.EUR,
             data_source='https://www.ecb.europa.eu/rss/fxref-isk.html',
        ),
        ECBExchangeRateScraper(
             source_currency=moneyed.NOK,
             target_currency=moneyed.EUR,
             data_source='https://www.ecb.europa.eu/rss/fxref-nok.html',
        ),
        ECBExchangeRateScraper(
             source_currency=moneyed.HRK,
             target_currency=moneyed.EUR,
             data_source='https://www.ecb.europa.eu/rss/fxref-hrk.html',
        ),
        ECBExchangeRateScraper(
             source_currency=moneyed.RUB,
             target_currency=moneyed.EUR,
             data_source='https://www.ecb.europa.eu/rss/fxref-rub.html',
        ),
        ECBExchangeRateScraper(
             source_currency=moneyed.TRY,
             target_currency=moneyed.EUR,
             data_source='https://www.ecb.europa.eu/rss/fxref-try.html',
        ),
        ECBExchangeRateScraper(
             source_currency=moneyed.AUD,
             target_currency=moneyed.EUR,
             data_source='https://www.ecb.europa.eu/rss/fxref-aud.html',
        ),
        ECBExchangeRateScraper(
             source_currency=moneyed.BRL,
             target_currency=moneyed.EUR,
             data_source='https://www.ecb.europa.eu/rss/fxref-brl.html',
        ),
        ECBExchangeRateScraper(
             source_currency=moneyed.CAD,
             target_currency=moneyed.EUR,
             data_source='https://www.ecb.europa.eu/rss/fxref-cad.html',
        ),
        ECBExchangeRateScraper(
             source_currency=moneyed.CNY,
             target_currency=moneyed.EUR,
             data_source='https://www.ecb.europa.eu/rss/fxref-cny.html',
        ),
        ECBExchangeRateScraper(
             source_currency=moneyed.HKD,
             target_currency=moneyed.EUR,
             data_source='https://www.ecb.europa.eu/rss/fxref-hkd.html',
        ),
        ECBExchangeRateScraper(
             source_currency=moneyed.IDR,
             target_currency=moneyed.EUR,
             data_source='https://www.ecb.europa.eu/rss/fxref-idr.html',
        ),
        ECBExchangeRateScraper(
             source_currency=moneyed.INR,
             target_currency=moneyed.EUR,
             data_source='https://www.ecb.europa.eu/rss/fxref-inr.html',
        ),
        ECBExchangeRateScraper(
             source_currency=moneyed.KRW,
             target_currency=moneyed.EUR,
             data_source='https://www.ecb.europa.eu/rss/fxref-krw.html',
        ),
        ECBExchangeRateScraper(
             source_currency=moneyed.MXN,
             target_currency=moneyed.EUR,
             data_source='https://www.ecb.europa.eu/rss/fxref-mxn.html',
        ),
        ECBExchangeRateScraper(
             source_currency=moneyed.MYR,
             target_currency=moneyed.EUR,
             data_source='https://www.ecb.europa.eu/rss/fxref-myr.html',
        ),
        ECBExchangeRateScraper(
             source_currency=moneyed.NZD,
             target_currency=moneyed.EUR,
             data_source='https://www.ecb.europa.eu/rss/fxref-nzd.html',
        ),
        ECBExchangeRateScraper(
             source_currency=moneyed.PHP,
             target_currency=moneyed.EUR,
             data_source='https://www.ecb.europa.eu/rss/fxref-php.html',
        ),
        ECBExchangeRateScraper(
             source_currency=moneyed.SGD,
             target_currency=moneyed.EUR,
             data_source='https://www.ecb.europa.eu/rss/fxref-sgd.html',
        ),
        ECBExchangeRateScraper(
             source_currency=moneyed.THB,
             target_currency=moneyed.EUR,
             data_source='https://www.ecb.europa.eu/rss/fxref-thb.html',
        ),
        ECBExchangeRateScraper(
             source_currency=moneyed.ZAR,
             target_currency=moneyed.EUR,
             data_source='https://www.ecb.europa.eu/rss/fxref-zar.html',
        ),
    ]

    for scraper in scrapers:
        scrape_exchange_rates(scraper)
