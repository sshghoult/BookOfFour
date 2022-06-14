## Abstract Factory
### Case description:
We are developing an app for a pizzeria which killer-feature is an option to cook their client a pizza by their custom recipe: 
pineapple, anchovy and some flaming pepper on the same slice? As you wish. 


However, internally for each such order we have to construct:
- recipe for the kitchen
- receipt for the checkout (each ingredient has its own price)
- allergy notice for the customers (depends on the ingredients)

Those are de-facto different representations of one entity and can be constructed step-by-step 
(with the step being an addition of the ingredient)