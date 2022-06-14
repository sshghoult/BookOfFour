## Abstract Factory
### Case description:
Logistics company has three possible physical ways to deliver the goods: 
by a track, by a container ship or by a plane. Each of the options includes certain specific transport characteristics, 
restrictions on the transported goods and pricing rules. 
Our goal is to neatly determine if the package can be sent this way and the cost
 of the delivery.

### Chosen level of decomposition:
- Transport - to describe physical limitations of the vessel used
- PackageRestrictions - to list restrictions on size and goods of the parcel
- PriceCalculator - to type-specifically calculate the price of the delivery

### Why?
Here we use Abstract Factory to ensure usage of only one class hierarchy in processing of each package 
and to keep the code clean by avoiding nasty repeated if-else-s intended to instantiate object of correct hierarchy by replacing them with
 choice of factory at the start, which then produces necessary objects.