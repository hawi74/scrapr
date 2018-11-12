from .models import ExchangeRate
from .scraper import ExchangeRateScraper


def scrape_exchange_rate(scraper: ExchangeRateScraper) -> None:
    exchange_rate = scraper.get_exchange_rate()

    if ExchangeRate.objects.filter(
        source_currency=exchange_rate.source_currency,
        target_currency=exchange_rate.target_currency,
        date=exchange_rate.date,
    ).exists():
        return

    model = ExchangeRate(
        source_currency=exchange_rate.source_currency,
        target_currency=exchange_rate.target_currency,
        rate=exchange_rate.rate,
        date=exchange_rate.date,
    )
    model.save()
