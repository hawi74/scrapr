from abc import ABC, abstractmethod
from dataclasses import dataclass
from decimal import Decimal
from datetime import datetime
from typing import List

import feedparser
from moneyed import Currency


@dataclass
class ExchangeRate:
    source_currency: Currency
    target_currency: Currency
    rate: Decimal
    datetime: datetime


class ExchangeRateScraper(ABC):

    @abstractmethod
    def get_exchange_rates(self) -> List[ExchangeRate]:
        ...


class ECBExchangeRateScraper(ExchangeRateScraper):

    def __init__(self, data_source, source_currency, target_currency):
        self.data_source = data_source
        self.source_currency = source_currency
        self.target_currency = target_currency

    def get_exchange_rates(self) -> List[ExchangeRate]:
        data = feedparser.parse(self.data_source)

        return [
            ExchangeRate(
                source_currency=self.source_currency,
                target_currency=self.target_currency,
                rate=self._parse_rate(entry.cb_exchangerate),
                datetime=datetime.fromisoformat(entry.updated),
            )
            for entry in data.entries
        ]

    def _parse_rate(self, rate):
        # rate from ECB is a string in following format: 12.3456USD
        return Decimal(rate[:-3])
