from abc import ABC, abstractmethod
from dataclasses import dataclass
from decimal import Decimal
from datetime import date

from moneyed import Currency


@dataclass
class ExchangeRate:
    source_currency: Currency
    target_currency: Currency
    rate: Decimal
    date: date


class ExchangeRateScraper(ABC):

    @abstractmethod
    def get_exchange_rate(self) -> ExchangeRate:
        ...
