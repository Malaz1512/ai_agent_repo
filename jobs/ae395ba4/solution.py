```python
class Character:
    """
    Base class for all game characters.

    Attributes:
        name (str): character's name.
        _health (int): current health points.
        _max_health (int): maximum health points.
        _level (int): character level.

    Invariants:
        - Health must be between 0 and max_health.
        - Max health must be greater than 0.
        - Level must be at least 1.
        - Name cannot be empty.

    Example usage:
    >>> char = Character("Hero", 100, 1)
    >>> print(char)
    Hero (Level 1) | HP: 100/100
    """

    def __init__(self, name: str, max_health: int, level: int) -> None:
        if not name:
            self._name = "Unknown"
        else:
            self._name = name

        if max_health <= 0:
            self._max_health = 1
        else:
            self._max_health = max_health

        if level < 1:
            self._level = 1
        else:
            self._level = level

        self._health = min(self._max_health, max(0, self._health))

    def get_health(self) -> int:
        """Returns current health."""
        return self._health

    def get_max_health(self) -> int:
        """Returns maximum health."""
        return self._max_health

    def get_level(self) -> int:
        """Returns character level."""
        return self._level

    def get_name(self) -> str:
        """Returns character's name."""
        return self._name

    def take_damage(self, damage: int) -> None:
        """Reduces health (cannot go below 0)."""
        if isinstance(damage, int) and damage > 0:
            self._health = max(0, self._health - damage)

    def heal(self, amount: int) -> None:
        """Increases health (cannot exceed max_health)."""
        if isinstance(amount, int) and amount > 0:
            self._health = min(self._max_health, self._health + amount)

    def is_alive(self) -> bool:
        """Returns True if health > 0."""
        return self._health > 0

    def __str__(self) -> str:
        """Returns a user-friendly string representation."""
        return f"{self._name} (Level {self._level}) | HP: {self._health}/{self._max_health}"

    def __repr__(self) -> str:
        """Returns a developer-friendly representation."""
        return (
            f"Character(name={self._name}, max_health={self._max_health}, "
            f"level={self._level})"
        )

    def __eq__(self, other: object) -> bool:
        """Compares characters by name."""
        if isinstance(other, Character):
            return self._name == other._name
        return False


class Warrior(Character):
    """
    Warrior class with armor reduction.

    Attributes:
        _armor (int): armor damage reduction.
    """

    def __init__(self, name: str, max_health: int, level: int, armor: int) -> None:
        super().__init__(name, max_health, level)
        self._armor = min(100, max(0, armor))

    def take_damage(self, damage: int) -> None:
        """Reduces damage by armor percentage."""
        reduced_damage = int(damage * (1 - self._armor / 100))
        super().take_damage(reduced_damage)

    def power_attack(self) -> str:
        """Returns a message about a powerful attack."""
        return f"{self.get_name()} performs a powerful attack!"

    def __str__(self) -> str:
        """Includes armor information in string representation."""
        base_str = super().__str__()
        return f"{base_str} | Armor: {self._armor}"


class Mage(Character):
    """
    Mage class with mana points.

    Attributes:
        _mana (int): current mana points.
        _max_mana (int): maximum mana points.
    """

    def __init__(self, name: str, max_health: int, level: int, max_mana: int) -> None:
        super().__init__(name, max_health, level)
        self._max_mana = max(1, max_mana)
        self._mana = self._max_mana

    def get_mana(self) -> int:
        """Returns current mana."""
        return self._mana

    def cast_spell(self, mana_cost: int) -> bool:
        """Uses mana if available."""
        if mana_cost <= self._mana:
            self._mana -= mana_cost
            return True
        return False

    def restore_mana(self, amount: int) -> None:
        """Restores mana (cannot exceed max_mana)."""
        if isinstance(amount, int) and amount > 0:
            self._mana = min(self._max_mana, self._mana + amount)

    def __str__(self) -> str:
        """Includes mana information in string representation."""
        base_str = super().__str__()
        return f"{base_str} | Mana: {self._mana}/{self._max_mana}"


class Archer(Character):
    """
    Archer class with arrow count.

    Attributes:
        _arrows (int): number of arrows.
    """

    def __init__(self, name: str, max_health: int, level: int, arrows: int) -> None:
        super().__init__(name, max_health, level)
        self._arrows = max(0, arrows)

    def get_arrows(self) -> int:
        """Returns arrow count."""
        return self._arrows

    def shoot_arrow(self) -> bool:
        """Uses one arrow if available."""
        if self._arrows > 0:
            self._arrows -= 1
            print(f"{self.get_name()} shoots an arrow!")
            return True
        print(f"{self.get_name()} has no arrows left!")
        return False

    def collect_arrows(self, amount: int) -> None:
        """Adds arrows (cannot exceed _arrows amount)."""
        if isinstance(amount, int) and amount > 0:
            self._arrows += amount

    def __str__(self) -> str:
        """Includes arrow count in string representation."""
        base_str = super().__str__()
        return f"{base_str} | Arrows: {self._arrows}"


class Item:
    """
    Item class representing an item in the game.

    Attributes:
        name (str): item name.
        _value (int): item value in gold.
        item_type (str): type of item (e.g., "weapon", "potion", "armor").
    """

    def __init__(self, name: str, value: int, item_type: str) -> None:
        self.name = name
        self._value = max(0, value)
        self.item_type = item_type

    def get_value(self) -> int:
        """Returns value."""
        return self._value

    def __str__(self) -> str:
        """Returns formatted item description."""
        return f"{self.name} ({self._value} gold)"

    def __eq__(self, other: object) -> bool:
        """Compares items by name."""
        if isinstance(other, Item):
            return self.name == other.name
        return False


class Inventory:
    """
    Inventory class representing a character's inventory.

    Attributes:
        _items (list[Item]): list of items.
        _max_capacity (int): maximum number of items.
    """

    def __init__(self, max_capacity: int) -> None:
        self._items = []
        self._max_capacity = max(1, max_capacity)

    def add_item(self, item: Item) -> bool:
        """Adds item if space available."""
        if len(self._items) < self._max_capacity:
            self._items.append(item)
            print(f"{item} added to inventory.")
            return True
        print("Inventory is full!")
        return False

    def remove_item(self, item_name: str) -> bool:
        """Removes item by name."""
        for i, item in enumerate(self._items):
            if item.name == item_name:
                del self._items[i]
                print(f"{item} removed from inventory.")
                return True
        print(f"Item {item_name} not found!")
        return False

    def get_item(self, item_name: str) -> Item | None:
        """Returns item if found."""
        for item in self._items:
            if item.name == item_name:
                return item
        return None

    def get_total_value(self) -> int:
        """Calculates total value of all items."""
        return sum(item.get_value() for item in self._items)

    def is_full(self) -> bool:
        """Returns True if inventory is at capacity."""
        return len(self._items) == self._max_capacity

    def __str__(self) -> str:
        """Includes item list in string representation."""
        items_str = ", ".join(str(item) for item in self._items)
        return f"Inventory: [{items_str}]"


class EnhancedCharacter(Character):
    """
    Enhanced character class with an inventory system.

    Attributes:
        inventory (Inventory): the character's inventory.
    """

    def __init__(self, name: str, max_health: int, level: int) -> None:
        super().__init__(name, max_health, level)
        self.inventory = Inventory(10)

    def add_to_inventory(self, item: Item) -> bool:
        """Adds an item to the inventory."""
        return self.inventory.add_item(item)

    def use_item(self, item_name: str) -> None:
        """Uses an item from the inventory."""
        item = self.inventory.get_item(item_name)
        if isinstance(item, Item):
            print(f"{self.get_name()} uses {item}!")
            # Example usage for a health potion
            if item.item_type == "potion":
                self.heal(50)
        else:
            print(f"Item {item_name} not found in inventory!")


def battle_simulation():
    """Simulates a battle scenario with different characters."""
    warrior = Warrior("Sir Galahad", 100, 1, 20)
    mage = Mage("Merlin", 80, 1, 100)
    archer = Archer("Robin Hood", 90, 1, 20)

    print("=== Battle Simulation ===")
    warrior.take_damage(20)
    print(warrior)  # Output: Sir Galahad takes 20 damage -> HP: 90/100 (armor absorbed 10 damage)

    if mage.cast_spell(30):
        print(f"{mage.get_name()} casts fireball for 30 mana -> Mana: {mage.get_mana()}/100")
    else:
        print(f"{mage.get_name()} does not have enough mana!")

    archer.shoot_arrow()
    print(archer)  # Output: Robin Hood shoots an arrow! | Arrows: 19/20


def inventory_system():
    """Demonstrates the inventory system with a character."""
    character = EnhancedCharacter("Robin Hood", 90, 1)
    health_potion = Item("Health Potion", 50, "potion")

    print("\n=== Inventory System ===")
    if character.add_to_inventory(health_potion):
        print(f"{character.get_name()} found a {health_potion}!")
    else:
        print(f"{character.get_name()}'s inventory is full!")

    print(character.inventory)  # Output: Inventory: [Health Potion (50 gold)]

    character.use_item("Health Potion")
    print(character)  # Output: Robin Hood uses Health Potion! | HP: 90/90 (already at max)


def main():
    """Main function to run the game simulation."""
    battle_simulation()
    inventory_system()


if __name__ == "__main__":
    main()
```