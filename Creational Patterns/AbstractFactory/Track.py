from .Abstract import AbstractDeliveryFactory, AbstractTransport, AbstractPackageRestrictions, AbstractPriceCalculator
from typing import Type, Collection, Tuple
from datetime import timedelta


class Truck(AbstractTransport):

    @property
    def volume(self) -> int:
        return 10 ** 3

    @property
    def delivery_time(self) -> timedelta:
        return timedelta(days=7)

    @property
    def delivery_price(self) -> int:
        return 10 ** 2


class TruckPackageRestrictions(AbstractPackageRestrictions):
    @property
    def size(self) -> Tuple[int, int, int]:
        return 100, 100, 100

    @property
    def prohibited_goods(self) -> Collection:
        return {'Human Body', 'Carpet', 'Human Body In a Carpet'}


class TruckPriceCalculator(AbstractPriceCalculator):
    def __init__(self, size: Tuple[int, int, int], weight: int):
        super().__init__()
        self._size = size
        self._volume = size[0] * size[1] * size[2]

        self._weight = weight

        self._insurance = None

        self._size_policy = 0.1
        self._weight_policy = 0.5


    def add_insurance(self, insurance_policy: 'AbstractInsurancePolicy'):
        self._insurance = insurance_policy

    def get_price(self):
        return max(self._size_policy * self._volume, self._weight_policy * self._weight) + self._insurance.get_price()


class TruckDeliveryFactory(AbstractDeliveryFactory):

    def get_transport(self) -> AbstractTransport:
        return Truck()

    def get_package_restrictions(self) -> AbstractPackageRestrictions:
        return TruckPackageRestrictions()

    def get_price_calculator(self) -> Type[AbstractPriceCalculator]:
        return TruckPriceCalculator
