from .models import ExchangeRate
from .scraper import ExchangeRateScraper, ExchangeRate as ExchangeRateData


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
