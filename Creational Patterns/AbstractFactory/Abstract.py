from abc import ABC, abstractmethod, ABCMeta
from typing import Type, Collection, Tuple
from datetime import timedelta


class AbstractTransport(ABC):

    @property
    @abstractmethod
    def volume(self) -> int:
        pass

    @property
    @abstractmethod
    def delivery_time(self) -> timedelta:
        pass


class AbstractPackageRestrictions(ABC):

    @property
    @abstractmethod
    def size(self) -> Tuple[int, int, int]:
        pass

    @property
    @abstractmethod
    def prohibited_goods(self) -> Collection:
        pass


class AbstractPriceCalculator(ABC):

    @abstractmethod
    def __init__(self, size: Tuple[int, int, int], weight: int):
        pass

    @abstractmethod
    def add_insurance(self, insurance_policy: 'AbstractInsurancePolicy'):
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


class BasePriceCalculator(AbstractPriceCalculator, metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, size: Tuple[int, int, int], weight: int):
        super().__init__(size, weight)
        self._size = size
        self._volume = size[0] * size[1] * size[2]

        self._weight = weight

        self._insurance = None

        self._size_policy: int = 0
        self._weight_policy: int = 0

    def add_insurance(self, insurance_policy: 'AbstractInsurancePolicy'):
        self._insurance = insurance_policy

    def get_price(self):
        price = max(self._size_policy * self._volume, self._weight_policy * self._weight)

        if self._insurance is not None:
            price += self._insurance.get_price()

        return price
