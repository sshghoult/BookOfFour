from .Abstract import AbstractDeliveryFactory, AbstractTransport, AbstractPackageRestrictions, AbstractPriceCalculator
from typing import Type

class PlaneDeliveryFactory(AbstractDeliveryFactory):
    def get_transport(self):
        pass

    def get_package_restrictions(self):
        pass

    def get_price_calculator(self):
        pass

