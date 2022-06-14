from abc import ABC, abstractmethod, ABCMeta


class AbstractPizzaRepresentationBuilder(ABC):
    @abstractmethod
    def start(self) -> None:
        pass

    @abstractmethod
    def add_crust(self, crust_type: str) -> None:
        pass

    @abstractmethod
    def add_base_sauce(self) -> None:
        pass

    @abstractmethod
    def add_chicken(self) -> None:
        pass

    @abstractmethod
    def add_pineapple(self) -> None:
        pass

    @abstractmethod
    def add_cheese(self, cheese_type: str) -> None:
        pass

    @abstractmethod
    def add_pepperoni(self) -> None:
        pass

    @abstractmethod
    def add_anchovy(self) -> None:
        pass

    @abstractmethod
    def add_hot_pepper(self) -> None:
        pass


class BasePizzaRepresentationBuilder(AbstractPizzaRepresentationBuilder):
    @abstractmethod
    def add_crust(self, crust_type: str) -> None:
        allowed_crusts = {'thin_crust', 'normal_crust', 'thick_crust'}
        if crust_type not in allowed_crusts:
            raise ValueError(f"{crust_type} type of crust is not whithin allowed options: {allowed_crusts}")

    @abstractmethod
    def add_cheese(self, cheese_type: str) -> None:
        allowed_cheeses = {'thin', 'normal', 'thick'}
        if cheese_type not in allowed_cheeses:
            raise ValueError(f"{cheese_type} type of cheese is not whithin allowed options: {allowed_cheeses}")


class PizzaReceipt:
    def __init__(self):
        self.ingredients = {}
        self.costs_per_ingredient = {}
        self.total = 0


class PizzaWarnings:
    def __init__(self):
        self.warnings = []
        self.is_vegetarian = True
        self.is_vegan = True
