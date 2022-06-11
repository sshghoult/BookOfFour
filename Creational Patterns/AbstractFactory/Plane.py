from datetime import timedelta

from .Abstract import AbstractDeliveryFactory, AbstractTransport, AbstractPackageRestrictions, AbstractPriceCalculator
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


class PlanePriceCalculator(AbstractPriceCalculator):

    def __init__(self, size, weight):
        super().__init__()
        self._size = size
        self._volume = size[0] * size[1] * size[2]

        self._weight = weight

        self._insurance = None

        self._size_policy = 0.7
        self._weight_policy = 0.9

    def add_insurance(self, insurance_policy: 'AbstractInsurancePolicy'):
        self._insurance = insurance_policy

    def get_price(self):
        return max(self._size_policy * self._volume, self._weight_policy * self._weight) + self._insurance.get_price()


class PlaneDeliveryFactory(AbstractDeliveryFactory):
    def get_transport(self) -> AbstractTransport:
        return Plane()

    def get_package_restrictions(self) -> AbstractPackageRestrictions:
        return PlanePackageRestrictions()

    def get_price_calculator(self) -> Type[AbstractPriceCalculator]:
        return PlanePriceCalculator
