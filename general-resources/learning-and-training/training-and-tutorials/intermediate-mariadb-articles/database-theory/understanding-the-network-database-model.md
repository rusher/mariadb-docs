
# Understanding the Network Database Model

The network database model was a progression from the [hierarchical database model](understanding-the-hierarchical-database-model.md) and was designed to solve some of that model's problems, specifically the lack of flexibility. Instead of only allowing each child to have one parent, this model allows each child to have multiple parents (it calls the children *members* and the parents *owners*). It addresses the need to model more complex relationships such as the orders/parts many-to-many relationship mentioned in the [hierarchical article](understanding-the-hierarchical-database-model.md). As you can see in the figure below, *A1* has two members, *B1* and *B2*. *B1.* is the owner of *C1*, *C2*, *C3* and *C4*. However, in this model, *C4* has two owners, *B1* and *B2*.


![network_model](../../../../../.gitbook/assets/understanding-the-network-database-model/+image/network_model.png "network_model")


Of course, this model has its problems, or everyone would still be using it. It is more difficult to implement and maintain, and, although more flexible than the hierarchical model, it still has flexibility problems, Not all relations can be satisfied by assigning another owner, and the programmer still has to understand the data structure well in order to make the model efficient.

