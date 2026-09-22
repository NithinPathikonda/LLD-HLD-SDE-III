# State Pattern (Behavioral)

## Industry Use Cases
- Vending machine states, Order lifecycles (Created -> Paid -> Shipped -> Delivered), Elevator states.

## Key SDE-III Structural Components
- State Interface, Concrete States, Context holding current State and transitioning cleanly.

## Implementation Checklist
- [ ] Abstract Base Class / Protocol defining the interface
- [ ] Concrete implementations with zero coupling to other implementations
- [ ] Context or Client class accepting abstraction
- [ ] Driver test verifying dynamic swapping at runtime
