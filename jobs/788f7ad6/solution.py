```python
import random

class Character:
    """
    Base class for all game characters.
    
    Attributes:
        name (str): character's name 
        _health (int): current health points 
        _max_health (int): maximum health points 
        _level (int): character level 
    
    Invariants:
        Health must be between 0 and max_health
        Max health must be greater than 0
        Level must be at least 1
        Name cannot be empty
    
    Args:
        name (str): The character's name.
        max_health (int): The character's maximum health.
        level (int): The character's level.
        
    Returns:
        None
    """
    
    def __init__(self, name: str, max_health: int, level: int) -> None:
        self.name = name
        self._max_health = max(1, max_health)
        self._health = min(max(self._max_health, 0), self._max_health)
        self._level = max(1, level)
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str) -> None:
        if not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value
    
    def get_health(self) -> int:
        """Returns current health."""
        return self._health
    
    def get_max_health(self) -> int:
        """Returns maximum health."""
        return self._max_health
    
    def get_level(self) -> int:
        """Returns character level."""
        return self._level
    
    def take_damage(self, damage: int) -> None:
        """Reduces health (cannot go below 0)."""
        if damage < 0:
            raise ValueError("Damage cannot be negative")
        self._health = max(0, self._health - damage)
    
    def heal(self, amount: int) -> None:
        """Increases health (cannot exceed max_health)."""
        if amount < 0:
            raise ValueError("Heal amount cannot be negative")
        self._health = min(self._max_health, self._health + amount)
    
    def is_alive(self) -> bool:
        """Returns True if health > 0."""
        return self._health > 0
    
    def __str__(self) -> str:
        """Returns a user-friendly string representation."""
        return f"{self.name} (Level {self._level}) | HP: {self._health}/{self._max_health}"
    
    def __repr__(self) -> str:
        """Returns a developer-friendly representation."""
        return f"Character(name={self.name!r}, max_health={self._max_health}, level={self._level})"
    
    def __eq__(self, other: object) -> bool:
        """Compares characters by name."""
        if isinstance(other, Character):
            return self.name == other.name
        return False

class Warrior(Character):
    """
    A warrior character with additional armor attribute.
    
    Attributes:
        _armor (int): armor damage reduction
    
    Invariants:
        Armor must be between 0 and 100
    """
    
    def __init__(self, name: str, max_health: int, level: int, armor: int) -> None:
        super().__init__(name, max_health, level)
        self._armor = min(100, max(0, armor))
    
    @property
    def _armor(self) -> int:
        return self.__armor
    
    @_armor.setter
    def _armor(self, value: int) -> None:
        if not (0 <= value <= 100):
            raise ValueError("Armor must be between 0 and 100")
        self.__armor = value
    
    def take_damage(self, damage: int) -> None:
        """Reduces damage by armor percentage."""
        reduced_damage = max(0, damage - (damage * self._armor / 100))
        super().take_damage(reduced_damage)
    
    def power_attack(self) -> str:
        """Returns a message about a powerful attack."""
        return f"{self.name} performs a powerful attack!"
    
    def __str__(self) -> str:
        """Includes armor information."""
        return f"{super().__str__()} | Armor: {self._armor}"

class Mage(Character):
    """
    A mage character with additional mana attributes.
    
    Attributes:
        _mana (int): current mana points
        _max_mana (int): maximum mana points
    
    Invariants:
        Mana must be between 0 and max_mana
        Max mana must be greater than 0
    """
    
    def __init__(self, name: str, max_health: int, level: int, max_mana: int) -> None:
        super().__init__(name, max_health, level)
        self._max_mana = max(1, max_mana)
        self._mana = min(max(self._max_mana, 0), self._max_mana)
    
    @property
    def _mana(self) -> int:
        return self.__mana
    
    @_mana.setter
    def _mana(self, value: int) -> None:
        if not (0 <= value <= self._max_mana):
            raise ValueError("Mana must be between 0 and max_mana")
        self.__mana = value
    
    def get_mana(self) -> int:
        """Returns current mana."""
        return self._mana
    
    def cast_spell(self, cost: int) -> bool:
        """Casts a spell if there is enough mana."""
        if self._mana >= cost:
            self._mana -= cost
            print(f"{self.name} casts fireball for {cost} mana")
            return True
        print(f"{self.name} does not have enough mana to cast the spell")
        return False
    
    def __str__(self) -> str:
        """Includes mana information."""
        return f"{super().__str__()} | Mana: {self._mana}/{self._max_mana}"

class Archer(Character):
    """
    An archer character with additional arrows attribute.
    
    Attributes:
        _arrows (int): number of arrows
    """
    
    def __init__(self, name: str, max_health: int, level: int) -> None:
        super().__init__(name, max_health, level)
        self._arrows = 20
    
    @property
    def _arrows(self) -> int:
        return self.__arrows
    
    @_arrows.setter
    def _arrows(self, value: int) -> None:
        if value < 0:
            raise ValueError("Arrows cannot be negative")
        self.__arrows = value
    
    def shoot_arrow(self) -> bool:
        """Shoots an arrow if there are any left."""
        if self._arrows > 0:
            self._arrows -= 1
            print(f"{self.name} shoots an arrow -> Arrows: {self._arrows}/20")
            return True
        print(f"{self.name} has no arrows left")
        return False
    
    def critical_hit(self) -> bool:
        """Returns True if a critical hit occurs (20% chance)."""
        return random.random() < 0.2
    
    def __str__(self) -> str:
        """Includes arrow information."""
        return f"{super().__str__()} | Arrows: {self._arrows}/20"

class Item:
    """
    Base class for items.
    
    Attributes:
        name (str): item's name
        value (int): item's value in gold
    
    Args:
        name (str): The item's name.
        value (int): The item's value in gold.
        
    Returns:
        None
    """
    
    def __init__(self, name: str, value: int) -> None:
        self.name = name
        self.value = value
    
    def __repr__(self) -> str:
        """Returns a developer-friendly representation."""
        return f"Item(name={self.name!r}, value={self.value})"

class Potion(Item):
    """
    A potion item that can be used to heal characters.
    
    Args:
        name (str): The potion's name.
        value (int): The potion's value in gold.
        heal_amount (int): The amount of health the potion heals.
        
    Returns:
        None
    """
    
    def __init__(self, name: str, value: int, heal_amount: int) -> None:
        super().__init__(name, value)
        self.heal_amount = heal_amount
    
    def __repr__(self) -> str:
        """Returns a developer-friendly representation."""
        return f"Potion(name={self.name!r}, value={self.value}, heal_amount={self.heal_amount})"

class Inventory:
    """
    An inventory that holds items.
    
    Attributes:
        capacity (int): the maximum number of items
        items (list[Item]): list of items in the inventory
    
    Args:
        capacity (int): The inventory's capacity.
        
    Returns:
        None
    """
    
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.items = []
    
    def add_item(self, item: Item) -> bool:
        """Adds an item to the inventory if it is not full."""
        if len(self.items) < self.capacity:
            self.items.append(item)
            print(f"{item.name} added to inventory!")
            return True
        print("Inventory is full")
        return False
    
    def remove_item(self, item_name: str) -> bool:
        """Removes an item by name from the inventory."""
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                print(f"{item.name} removed from inventory.")
                return True
        print(f"{item_name} not found in inventory.")
        return False
    
    def get_item(self, item_name: str) -> Item | None:
        """Returns an item by name if it exists in the inventory."""
        for item in self.items:
            if item.name == item_name:
                return item
        return None
    
    def get_total_value(self) -> int:
        """Calculates total value of all items."""
        return sum(item.value for item in self.items)
    
    def is_full(self) -> bool:
        """Returns True if the inventory is at capacity."""
        return len(self.items) >= self.capacity
    
    def list_items(self) -> None:
        """Prints all items in the inventory."""
        if not self.items:
            print("Inventory is empty")
        for item in self.items:
            print(f"- {item.name} ({item.value} gold)")
    
    def __str__(self) -> str:
        """Returns a formatted inventory summary."""
        return f"Inventory: [{', '.join(item.name for item in self.items)}]"

class EnhancedCharacter(Character):
    """
    An enhanced character with an inventory.
    
    Attributes:
        name (str): character's name 
        max_health (int): character's maximum health
        level (int): character's level
        inventory (Inventory): the character's inventory
    
    Args:
        name (str): The character's name.
        max_health (int): The character's maximum health.
        level (int): The character's level.
        
    Returns:
        None
    """
    
    def __init__(self, name: str, max_health: int, level: int) -> None:
        super().__init__(name, max_health, level)
        self.inventory = Inventory(10)
    
    def add_item_to_inventory(self, item: Item) -> bool:
        """Adds an item to the character's inventory."""
        return self.inventory.add_item(item)
    
    def use_potion(self, potion_name: str) -> bool:
        """Heals the character by 20 HP if a potion is found in the inventory."""
        potion = self.inventory.get_item(potion_name)
        if isinstance(potion, Potion):
            self.heal(20)
            print(f"{self.name} uses {potion_name} -> HP: {self._health}/{self._max_health}")
            self.inventory.remove_item(potion_name)
            return True
        print(f"No {potion_name} found in inventory.")
        return False
    
    def __str__(self) -> str:
        """Includes inventory item count."""
        return f"{super().__str__()} | Inventory: {len(self.inventory.items)}/10"

def battle_simulation(characters: list[Character]) -> None:
    """
    Simulates a battle with various character types.
    
    Args:
        characters (list[Character]): A list of different character types.
        
    Returns:
        None
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

def main():
    """
    Main function to demonstrate the game features.
    
    Returns:
        None
    """
    # Creating characters
    warrior = Warrior("Sir Galahad", 100, 1, 50)
    mage = Mage("Merlin the Wise", 80, 1, 100)
    archer = Archer("Robin Hood", 90, 1)
    
    # Testing character methods
    print("=== Creating Characters ===")
    print(warrior)
    print(mage)
    print(archer)
    
    warrior.take_damage(10)
    mage.take_damage(5)
    archer.take_damage(8)
    
    print("\nAfter taking damage:")
    print(warrior)
    print(mage)
    print(archer)
    
    # Inventory system
    health_potion = Potion("Health Potion", 50, 20)
    mana_potion = Potion("Mana Potion", 30, 10)
    
    warrior.add_item_to_inventory(health_potion)
    mage.add_item_to_inventory(mana_potion)
    archer.add_item_to_inventory(health_potion)
    
    print("\n=== Inventory System ===")
    archer.inventory.list_items()
    archer.use_potion("Health Potion")
    archer.inventory.list_items()
    
    # Battle simulation
    battle_simulation([warrior, mage, archer])
    
    # Testing __eq__
    warrior2 = Warrior("Sir Galahad", 100, 1, 50)
    print("\nTesting __eq__:")
    print(warrior == warrior2)  # True
    
    # Demonstrating polymorphism
    characters = [warrior, mage, archer]
    for character in characters:
        if isinstance(character, Warrior):
            print(f"{character.name} is a Warrior")
        elif isinstance(character, Mage):
            print(f"{character.name} is a Mage")
        elif isinstance(character, Archer):
            print(f"{character.name} is an Archer")

if __name__ == "__main__":
    main()