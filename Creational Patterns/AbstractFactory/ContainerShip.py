from datetime import timedelta

from .Abstract import AbstractDeliveryFactory, AbstractTransport, AbstractPackageRestrictions, AbstractPriceCalculator
from typing import Type, Collection, Tuple


class ContainerShip(AbstractTransport):

    @property
    def volume(self) -> int:
        return 10 ** 10

    @property
    def delivery_time(self) -> timedelta:
        return timedelta(days=28)


class ContainerShipPackageRestrictions(AbstractPackageRestrictions):

    @property
    def size(self) -> Tuple[int, int, int]:
        return 10000, 10000, 10000

    @property
    def prohibited_goods(self) -> Collection:
        return {'Whale', 'Container Ship'}


class ContainerShipPriceCalculator(AbstractPriceCalculator):

    def __init__(self, size, weight):
        super().__init__()
        self._size = size
        self._volume = size[0] * size[1] * size[2]

        self._weight = weight

        self._insurance = None

        self._size_policy = 0
        self._weight_policy = 0.3

    def add_insurance(self, insurance_policy: 'AbstractInsurancePolicy'):
        self._insurance = insurance_policy

    def get_price(self):
        return max(self._size_policy * self._volume, self._weight_policy * self._weight) + self._insurance.get_price()


class ContainerShipDeliveryFactory(AbstractDeliveryFactory):
    def get_transport(self) -> AbstractTransport:
        return ContainerShip()

    def get_package_restrictions(self) -> AbstractPackageRestrictions:
        return ContainerShipPackageRestrictions()

    def get_price_calculator(self) -> Type[AbstractPriceCalculator]:
        return ContainerShipPriceCalculator
