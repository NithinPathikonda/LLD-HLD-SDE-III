# Factory & Abstract Factory Pattern (Creational)

## Industry Use Cases
- Vehicle creation in Parking Lot, Notification channel factory (SMS/Email/Push), Cloud client factory (AWS/GCP/Azure).

## Key SDE-III Structural Components
- Product Interface, Concrete Products, Factory Method or Abstract Factory with registration decorator.

## Implementation Checklist
- [ ] Abstract Base Class / Protocol defining the interface
- [ ] Concrete implementations with zero coupling to other implementations
- [ ] Context or Client class accepting abstraction
- [ ] Driver test verifying dynamic swapping at runtime
