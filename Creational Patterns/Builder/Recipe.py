from Abstract import BasePizzaRepresentationBuilder
from collections import Counter


class PizzaRecipe:
    def __init__(self):
        self.instructions = []
        self.ingredients = Counter()


class PizzaRecipeBuilder(BasePizzaRepresentationBuilder):

    def __init__(self):
        self._product = PizzaRecipe()


    def start(self) -> None:
        self._product.instructions.append(f"Clear the kitchen and prepare your instruments.")

    def finish(self) -> PizzaRecipe:
        self._product.instructions.append(f"Prepare the pizza to be served")
        return self._product

    def add_crust(self, crust_type: str) -> None:
        super().add_crust(crust_type)

        self._product.ingredients[crust_type] += 1
        self._product.instructions.append(f"Prepare this crust: {crust_type}")

    def add_cheese(self, cheese_type: str) -> None:
        super().add_cheese(cheese_type)

        self._product.ingredients[cheese_type] += 1
        self._product.instructions.append(f"Add a portion of this cheese: {cheese_type}")


    def add_base_sauce(self) -> None:
        self._product.ingredients['base_sauce'] += 1
        self._product.instructions.append(f"Add a portion of the base sauce")

    def add_chicken(self) -> None:
        self._product.ingredients['chicken'] += 1
        self._product.instructions.append(f"Add a portion of the slices of chicken meat")


    def add_pineapple(self) -> None:
        self._product.ingredients['pineapple'] += 1
        self._product.instructions.append(f"Add a portion of the slices of pineapple")

    def add_pepperoni(self) -> None:
        self._product.ingredients['pepperoni'] += 1
        self._product.instructions.append(f"Add a portion of the pepperoni")

    def add_anchovy(self) -> None:
        self._product.ingredients['anchovy'] += 1
        self._product.instructions.append(f"Add a portion of anchovy")

    def add_hot_pepper(self) -> None:
        self._product.ingredients['pepper'] += 1
        self._product.instructions.append(f"Add a portion of pepper")
