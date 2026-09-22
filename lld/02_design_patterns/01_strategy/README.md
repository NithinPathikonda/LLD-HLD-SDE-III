# Strategy Pattern (Behavioral)

## Industry Use Cases
- Dynamic fee calculation in Parking Lot, Route planners (Fastest vs Shortest), Payment processing (UPI vs Card vs NetBanking).

## Key SDE-III Structural Components
- Strategy Interface, Concrete Strategies, Context class accepting strategy.

## Implementation Checklist
- [ ] Abstract Base Class / Protocol defining the interface
- [ ] Concrete implementations with zero coupling to other implementations
- [ ] Context or Client class accepting abstraction
- [ ] Driver test verifying dynamic swapping at runtime
