from Abstract import *
from Track import *
from Plane import *
from ContainerShip import *


class Parcel:
    def __init__(self, length: int, width: int, height: int, weight: int, product: str):
        self.length = length
        self.width = width
        self.height = height

        self.volume = length * width * height

        self.product = product

        self.weight = weight

    def size(self) -> Tuple[int, int, int]:
        return self.length, self.width, self.height


def main(delivery_option: str):
    goods = Parcel(10, 10, 10, 5, 'Human Body')

    factory: AbstractDeliveryFactory = None

    if delivery_option == 'container_ship':
        factory = ContainerShipDeliveryFactory()
    elif delivery_option == 'truck':
        factory = TruckDeliveryFactory()
    elif delivery_option == 'plane':
        factory = PlaneDeliveryFactory()

    transport = factory.get_transport()

    restrictions = factory.get_package_restrictions()

    can_be_sent_flag = transport.volume >= goods.volume and (goods.product not in restrictions.prohibited_goods)

    can_be_sent_flag = can_be_sent_flag and all(a >= b for a, b in zip(restrictions.size, goods.size()))

    if not can_be_sent_flag:
        raise ValueError

    calculator_class = factory.get_price_calculator()
    calculator = calculator_class(goods.size(), goods.weight)
    return calculator.get_price()


if __name__ == '__main__':
    print(main('plane'))
