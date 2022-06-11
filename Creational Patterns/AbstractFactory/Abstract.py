from abc import ABC, abstractmethod
from typing import Type, Collection, Tuple
from datetime import timedelta


class AbstractTransport(ABC):

    @abstractmethod
    @property
    def volume(self) -> int:
        pass

    @abstractmethod
    @property
    def delivery_time(self) -> timedelta:
        pass

    @abstractmethod
    @property
    def delivery_price(self) -> int:
        pass


class AbstractPackageRestrictions(ABC):

    @abstractmethod
    @property
    def size(self) -> Tuple[int, int, int]:
        pass

    @abstractmethod
    @property
    def prohibited_goods(self) -> Collection:
        pass


class AbstractPriceCalculator(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def add_insurance(self, insurance_policy):
        pass

    @abstractmethod
    def get_price(self):
        pass


class AbstractDeliveryFactory(ABC):

    @abstractmethod
    def get_transport(self) -> AbstractTransport:
        pass

    @abstractmethod
    def get_package_restrictions(self) -> AbstractPackageRestrictions:
        pass

    @abstractmethod
    def get_price_calculator(self) -> Type[AbstractPriceCalculator]:
        pass
