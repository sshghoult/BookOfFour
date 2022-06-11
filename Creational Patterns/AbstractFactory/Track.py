from Abstract import AbstractDeliveryFactory, AbstractTransport, AbstractPackageRestrictions, AbstractPriceCalculator, BasePriceCalculator
from typing import Type, Collection, Tuple
from datetime import timedelta


class Truck(AbstractTransport):

    @property
    def volume(self) -> int:
        return 10 ** 3

    @property
    def delivery_time(self) -> timedelta:
        return timedelta(days=7)


class TruckPackageRestrictions(AbstractPackageRestrictions):
    @property
    def size(self) -> Tuple[int, int, int]:
        return 100, 100, 100

    @property
    def prohibited_goods(self) -> Collection:
        return {'Human Body', 'Carpet', 'Human Body In a Carpet'}


class TruckPriceCalculator(BasePriceCalculator):
    def __init__(self, size: Tuple[int, int, int], weight: int):
        super().__init__(size, weight)

        self._size_policy = 0.1
        self._weight_policy = 0.5



class TruckDeliveryFactory(AbstractDeliveryFactory):

    def get_transport(self) -> AbstractTransport:
        return Truck()

    def get_package_restrictions(self) -> AbstractPackageRestrictions:
        return TruckPackageRestrictions()

    def get_price_calculator(self) -> Type[AbstractPriceCalculator]:
        return TruckPriceCalculator
