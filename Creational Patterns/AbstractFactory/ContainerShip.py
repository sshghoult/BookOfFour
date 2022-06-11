from datetime import timedelta

from Abstract import AbstractDeliveryFactory, AbstractTransport, AbstractPackageRestrictions, AbstractPriceCalculator, BasePriceCalculator
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


class ContainerShipPriceCalculator(BasePriceCalculator):

    def __init__(self, size, weight):
        super().__init__(size, weight)

        self._size_policy = 0
        self._weight_policy = 0.3



class ContainerShipDeliveryFactory(AbstractDeliveryFactory):
    def get_transport(self) -> AbstractTransport:
        return ContainerShip()

    def get_package_restrictions(self) -> AbstractPackageRestrictions:
        return ContainerShipPackageRestrictions()

    def get_price_calculator(self) -> Type[AbstractPriceCalculator]:
        return ContainerShipPriceCalculator
