from datetime import timedelta

from .Abstract import AbstractDeliveryFactory, AbstractTransport, AbstractPackageRestrictions, AbstractPriceCalculator, BasePriceCalculator
from typing import Type, Collection, Tuple


class Plane(AbstractTransport):

    @property
    def volume(self) -> int:
        return 10 ** 5

    @property
    def delivery_time(self) -> timedelta:
        return timedelta(days=1)


class PlanePackageRestrictions(AbstractPackageRestrictions):

    @property
    def size(self) -> Tuple[int, int, int]:
        return 1000, 1000, 450

    @property
    def prohibited_goods(self) -> Collection:
        return {'Manicure Scissors', 'Duty Free Scotch'}


class PlanePriceCalculator(BasePriceCalculator):

    def __init__(self, size, weight):
        super().__init__(size, weight)

        self._size_policy = 0.7
        self._weight_policy = 0.9


class PlaneDeliveryFactory(AbstractDeliveryFactory):
    def get_transport(self) -> AbstractTransport:
        return Plane()

    def get_package_restrictions(self) -> AbstractPackageRestrictions:
        return PlanePackageRestrictions()

    def get_price_calculator(self) -> Type[AbstractPriceCalculator]:
        return PlanePriceCalculator
