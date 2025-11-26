```python
class Character:
    """
    Represents a basic character in the RPG game.
    
    Attributes:
        name (str): The character's name.
        _health (int): The current health points of the character.
        _max_health (int): The maximum health points of the character.
        _level (int): The level of the character.
        
    Invariants:
        - Health must be between 0 and max_health
        - Max health must be greater than 0
        - Level must be at least 1
        - Name cannot be empty
    """
    
    def __init__(self, name: str, max_health: int = 100, level: int = 1) -> None:
        self.name = name
        self._health = max(0, min(max_health, max_health))
        self._max_health = max(1, max_health)
        self._level = max(1, level)
        
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str) -> None:
        if not value.isalpha() and not all(c in " -'" for c in value):
            raise ValueError("Name must be alphabetic with spaces, hyphens, or apostrophes.")
        self._name = value
    
    def get_health(self) -> int:
        """Returns the current health of the character."""
        return self._health
    
    def get_max_health(self) -> int:
        """Returns the maximum health of the character."""
        return self._max_health
    
    def get_level(self) -> int:
        """Returns the level of the character."""
        return self._level
    
    def take_damage(self, damage: int) -> None:
        """Reduces health by the given amount, cannot go below 0."""
        self._health = max(0, self._health - damage)
    
    def heal(self, amount: int) -> None:
        """Increases health by the given amount, cannot exceed max_health."""
        self._health = min(self._max_health, self._health + amount)
    
    def is_alive(self) -> bool:
        """Returns True if the character's health is greater than 0."""
        return self._health > 0
    
    def __str__(self) -> str:
        """Returns a user-friendly string representation of the character."""
        return f"{self.name} (Level {self._level}) | HP: {self._health}/{self._max_health}"
    
    def __repr__(self) -> str:
        """Returns a developer-friendly representation of the character."""
        return f"Character(name={self.name!r}, max_health={self._max_health}, level={self._level})"
    
    def __eq__(self, other: object) -> bool:
        """Compares characters by name."""
        if isinstance(other, Character):
            return self.name == other.name
        return False

class Warrior(Character):
    """
    Represents a Warrior character in the RPG game.
    
    Inherits from Character and adds armor attribute.
    """
    
    def __init__(self, name: str, max_health: int = 120, level: int = 1, armor: int = 50) -> None:
        super().__init__(name, max_health, level)
        self._armor = min(100, max(0, armor))
    
    @property
    def armor(self) -> int:
        return self._armor
    
    def take_damage(self, damage: int) -> None:
        """Reduces damage by armor percentage before applying it."""
        reduced_damage = max(0, damage - (damage * self._armor / 100))
        super().take_damage(reduced_damage)
    
    def power_attack(self) -> str:
        """Returns a message about a powerful attack."""
        return f"{self.name} delivers a mighty blow!"
    
    def __str__(self) -> str:
        """Includes armor information in the string representation."""
        return f"{super().__str__()} | Armor: {self._armor}"

class Mage(Character):
    """
    Represents a Mage character in the RPG game.
    
    Inherits from Character and adds mana attributes.
    """
    
    def __init__(self, name: str, max_health: int = 80, level: int = 1, max_mana: int = 100) -> None:
        super().__init__(name, max_health, level)
        self._mana = min(max_mana, max(0, max_mana))
        self._max_mana = max(1, max_mana)
    
    def get_mana(self) -> int:
        """Returns the current mana of the Mage."""
        return self._mana
    
    def cast_spell(self, mana_cost: int) -> bool:
        """Uses mana if available, returns True if successful."""
        if self._mana >= mana_cost:
            self._mana -= mana_cost
            print(f"{self.name} casts a spell for {mana_cost} mana.")
            return True
        else:
            print(f"{self.name} does not have enough mana to cast the spell.")
            return False
    
    def restore_mana(self, amount: int) -> None:
        """Restores mana by the given amount, cannot exceed max_mana."""
        self._mana = min(self._max_mana, self._mana + amount)
    
    def __str__(self) -> str:
        """Includes mana information in the string representation."""
        return f"{super().__str__()} | Mana: {self._mana}/{self._max_mana}"

class Archer(Character):
    """
    Represents an Archer character in the RPG game.
    
    Inherits from Character and adds arrows attribute.
    """
    
    def __init__(self, name: str, max_health: int = 90, level: int = 1, arrows: int = 20) -> None:
        super().__init__(name, max_health, level)
        self._arrows = max(0, arrows)
    
    def get_arrows(self) -> int:
        """Returns the number of arrows."""
        return self._arrows
    
    def shoot_arrow(self) -> bool:
        """Uses one arrow if available, prints a message, and returns True if successful."""
        if self._arrows > 0:
            self._arrows -= 1
            print(f"{self.name} shoots an arrow.")
            return True
        else:
            print(f"{self.name} has no arrows left.")
            return False
    
    def __str__(self) -> str:
        """Includes arrow count in the string representation."""
        return f"{super().__str__()} | Arrows: {self._arrows}"

class Item:
    """
    Represents an item that can be added to a character's inventory.
    
    Attributes:
        name (str): The name of the item.
        value (int): The value or effect of the item.
    """
    
    def __init__(self, name: str, value: int) -> None:
        self.name = name
        self.value = value
    
    def __repr__(self) -> str:
        """Returns a developer-friendly representation of the item."""
        return f"Item(name={self.name!r}, value={self.value})"

class CharacterWithInventory(Character):
    """
    Extends the Character class to include an inventory.
    
    Attributes:
        inventory (list[Item]): The list of items in the character's inventory.
    """
    
    def __init__(self, name: str, max_health: int = 100, level: int = 1) -> None:
        super().__init__(name, max_health, level)
        self.inventory = []
    
    def add_item(self, item: Item) -> None:
        """Adds an item to the character's inventory."""
        self.inventory.append(item)
    
    def use_potion(self) -> None:
        """Heals the character by 20 HP if a potion is found in the inventory."""
        for item in self.inventory:
            if "potion" in item.name.lower():
                self.heal(20)
                print(f"{self.name} uses {item.name} -> HP: {self._health}/{self._max_health}")
                self.inventory.remove(item)
                return
        print(f"{self.name} has no potions to use.")
    
    def __str__(self) -> str:
        """Includes inventory item count in the string representation."""
        item_count = len(self.inventory)
        return f"{super().__str__()} | Inventory: {item_count} items"

def battle_simulation(characters: list[Character]) -> None:
    """
    Simulate a battle with various character types.
    
    Parameters:
        characters (list[Character]): A list of different character types.
    """
    print("=== Battle Simulation ===")
    for character in characters:
        print(character)  # Polymorphism: different __str__ for each type
        character.take_damage(20)  # Polymorphism: Warriors take less damage
        
        if isinstance(character, Warrior):
            print(character.power_attack())
        elif isinstance(character, Mage):
            character.cast_spell(10)
        elif isinstance(character, Archer):
            character.shoot_arrow()

def main() -> None:
    """
    Main function to demonstrate the RPG game functionality.
    """
    print("=== Creating Characters ===")
    
    warrior = Warrior("Sir Galahad", armor=50)
    mage = Mage("Merlin the Wise", max_mana=100)
    archer = Archer("Robin Hood", arrows=20)
    
    characters = [warrior, mage, archer]
    
    for character in characters:
        print(character)
    
    battle_simulation(characters)
    
    print("\n=== Inventory System ===")
    
    health_potion = Item("Health Potion", 50)
    mana_potion = Item("Mana Potion", 20)
    
    archer.add_item(health_potion)
    mage.add_item(mana_potion)
    
    for character in characters:
        print(f"{character.name} found a {health_potion.name}!")
    
    archer.use_potion()
    mage.use_potion()
    
    for character in characters:
        print(character)

if __name__ == "__main__":
    main()
```