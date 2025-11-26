# Unit 3 Practice Lab

## Scenario
You are building a role-playing game (RPG) system. Your game needs different types of characters, each with unique abilities, an inventory system, and equipment. You'll use object-oriented programming principles to create a flexible, maintainable system.

---

## Part 1: Basic Character Class 
Create a `Character` class that serves as the base for all game characters.

### Requirements:
1. **Attributes** (all should be properly encapsulated):
   - `name` (str): character's name 
   - `_health` (int): current health points 
   - `_max_health` (int): maximum health points 
   - `_level` (int): character level 

2. **Invariants** (document these in the class docstring):
   - Health must be between 0 and max_health
   - Max health must be greater than 0
   - Level must be at least 1
   - Name cannot be empty

3. **Methods**:
   - `__init__(self, name: str, max_health: int, level: int) -> None`
     - Validate all invariants
     - Set default values for invalid inputs (ex., level defaults to 1)
   - `get_health(self) -> int`: returns current health
   - `get_max_health(self) -> int`: returns maximum health
   - `get_level(self) -> int`: returns level
   - `get_name(self) -> str`: returns name
   - `take_damage(self, damage: int) -> None`: reduces health (cannot go below 0)
   - `heal(self, amount: int) -> None`: increases health (cannot exceed max_health)
   - `is_alive(self) -> bool`: returns True if health > 0
   - `__str__(self) -> str`: returns a user-friendly string representation
   - `__repr__(self) -> str`: returns a developer-friendly representation
   - `__eq__(self, other: object) -> bool`: compares characters by name

4. **Documentation**:
   - Include a comprehensive class docstring
   - Add type annotations to all methods
   - Write docstrings for each method with Args and Returns sections
   - Include at least one doctest example in your class docstring

---

## Part 2: Character Inheritance
Create three child classes that inherit from `Character`: `Warrior`, `Mage`, and `Archer`.

### Warrior Class:
- **Additional Attributes**:
  - `_armor` (int): armor damage reduction
- **Invariants**:
  - Armor must be between 0 and 100
- **Methods**:
  - Override `__init__` using `super()` and adding the new attribute
  - Override `take_damage()`: reduce damage by armor percentage (e.g., 50 armor = 50% damage reduction)
  - `power_attack(self) -> str`: returns a message about a powerful attack
  - Override `__str__()` to include armor information

### Mage Class:
- **Additional Attributes**:
  - `_mana` (int): current mana points
  - `_max_mana` (int): maximum mana points
- **Invariants**:
  - Mana must be between 0 and max_mana
  - Max mana must be greater than 0
- **Methods**:
  - Override `__init__` using `super()` and adding the new attributes
  - `get_mana(self) -> int`: returns current mana
  - `cast_spell(self, mana_cost: int) -> bool`: uses mana if available, returns True if successful
  - `restore_mana(self, amount: int) -> None`: restores mana (cannot exceed max_mana)
  - Override `__str__()` to include mana information

### Archer Class:
- **Additional Attributes**:
  - `_arrows` (int): number of arrows
- **Invariants**:
  - Arrows cannot be negative
- **Methods**:
  - Override `__init__` using `super()` and adding the new attribute
  - `get_arrows(self) -> int`: returns arrow count
  - `shoot_arrow(self) -> bool`: uses one arrow if available, print a message, and returns True if successful
  - `collect_arrows(self, amount: int) -> None`: adds arrows, cannot exceed _arrows amount
  - Override `__str__()` to include arrow count

**Requirements for all child classes**:
- Use `super().__init__()` to call the parent constructor
- Include proper documentation with type annotations
- Validate all invariants in constructors

---

## Part 3: Composition 
Create an `Item` class and an `Inventory` class to demonstrate composition.

### Item Class:
- **Attributes**:
  - `name` (str): item name
  - `_value` (int): item value in gold
  - `item_type` (str): type of item (e.g., "weapon", "potion", "armor")
- **Methods**:
  - `__init__(self, name: str, value: int, item_type: str) -> None`
  - `get_value(self) -> int`: returns value
  - `__str__(self) -> str`: returns formatted item description
  - `__eq__(self, other: object) -> bool`: compares items by name

### Inventory Class 
- **Attributes**:
  - `_items` (list[Item]): list of items
  - `_max_capacity` (int): maximum number of items 
- **Methods**:
  - `__init__(self, max_capacity: int) -> None`
  - `add_item(self, item: Item) -> bool`: adds item if space available, print a message, and returns True if successful
  - `remove_item(self, item_name: str) -> bool`: removes item by name, print a message, and returns True if found
  - `get_item(self, item_name: str) -> Item | None`: returns item if found, None otherwise
  - `get_total_value(self) -> int`: calculates total value of all items
  - `is_full(self) -> bool`: returns True if inventory is at capacity
  - `list_items(self) -> None`: prints all items in inventory
  - `__str__(self) -> str`: returns formatted inventory summary

---

## Part 4: Enhanced Character with Inventory
Modify your `Character` class to include an inventory:
1. Add an `inventory` attribute of type `Inventory` (composition)
2. Update the `__init__` method to create an inventory with capacity 10
3. Add these methods:
   - `add_item_to_inventory(self, item: Item) -> bool`
   - `use_potion(self, potion_name: str) -> bool`: heals character by 20 HP if potion found in inventory, removes potion after use
4. Update the `__str__` method to show inventory item count

---

## Part 5: Polymorphism Demonstration

Create a function called `battle_simulation(characters: list[Character]) -> None` that:
1. Takes a list of different character types (Warrior, Mage, Archer)
2. Uses `isinstance()` to check character types
3. Calls appropriate methods based on character type (polymorphism)
4. Prints battle information using each character's `__str__` method
5. Demonstrates that the same method call (like `take_damage()`) works differently for different character types

Example structure:
```python
def battle_simulation(characters: list[Character]) -> None:
    """Simulate a battle with various character types."""
    for character in characters:
        print(character)  # Polymorphism: different __str__ for each type
        character.take_damage(20)  # Polymorphism: Warriors take less damage
        
        if isinstance(character, Warrior):
            print(character.power_attack())
        elif isinstance(character, Mage):
            character.cast_spell(10)
        elif isinstance(character, Archer):
            character.shoot_arrow()
```

---

## Part 6: Testing and Main Program 

Create a `main()` function that demonstrates:
1. Creating at least one instance of each character type
2. Testing all methods of each class
3. Adding items to character inventories
4. Using potions to heal characters
5. Calling your `battle_simulation()` function
6. Testing `__eq__` by comparing characters
7. Using `isinstance()` and demonstrating polymorphism

---

## Bonus 
1. **Level Up System**: Add a `level_up()` method to `Character` that increases level and max_health
2. **Critical Hits**: Add a method to Archer that has a 20% chance of critical hit (double damage)
3. **Spell System**: Create a `Spell` class and have Mage store a list of learnable spells
4. **Equipment System**: Create `Weapon` and `Armor` classes that characters can equip
5. **Save/Load System**: Implement methods to save character data to a file and load it back

## Example Output

```
=== Creating Characters ===
Sir Galahad (Level 1) | HP: 100/100 | Armor: 50
Merlin the Wise (Level 1) | HP: 80/80 | Mana: 100/100
Robin Hood (Level 1) | HP: 90/90 | Arrows: 20

=== Battle Simulation ===
Sir Galahad takes 20 damage -> HP: 90/100 (armor absorbed 10 damage)
Merlin casts fireball for 30 mana -> Mana: 70/100
Robin shoots an arrow -> Arrows: 19/20

=== Inventory System ===
Robin found a Health Potion!
Inventory: [Health Potion (50 gold)]
Robin uses Health Potion -> HP: 90/90 (already at max)
```
