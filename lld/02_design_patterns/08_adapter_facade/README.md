# Adapter & Facade Pattern (Structural)

## Industry Use Cases
- Adapter: Translating third-party legacy XML payment response to internal JSON format. Facade: Simplified unified API over complex subsystem.

## Key SDE-III Structural Components
- Target interface, Adaptee (incompatible), Adapter implementing Target and wrapping Adaptee.

## Implementation Checklist
- [ ] Abstract Base Class / Protocol defining the interface
- [ ] Concrete implementations with zero coupling to other implementations
- [ ] Context or Client class accepting abstraction
- [ ] Driver test verifying dynamic swapping at runtime
