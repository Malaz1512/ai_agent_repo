Here is the output only valid Python code for the instructions:

```Python
class Character:
    def __init__(self, name: str, max_health: int, level: int) -> None:
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if level < 1:
            level = 1
        self._name = name
        self._health = max_health
        self._max_health = max_health
        self._level = level

    @property
    def health(self) -> int:
        return self._health

    @property
    def max_health(self) -> int:
        return self._max_health

    @property
    def level(self) -> int:
        return self._level

    @property
    def name(self) -> str:
        return self._name

    def take_damage(self, damage: int) -> None:
        if self._health <= 0:
            raise ValueError("Character is already dead")
        if damage < 0:
            raise ValueError("Damage must be a positive integer")
        self._health -= damage
        if self._health < 0:
            self._health = 0

    def heal(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("Healing amount must be a positive integer")
        if amount > self._max_health - self._health:
            self._health = self._max_health
        else:
            self._health += amount

    def is_alive(self) -> bool:
        return self._health > 0

    def __str__(self) -> str:
        return f"{self.name} (Level {self.level}) | HP: {self.health}/{self.max_health}"

    def __repr__(self) -> str:
        return f"Character('{self.name}', {self.max_health}, {self.level})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Character):
            return False
        return self._name == other._name


class Warrior(Character):
    def __init__(self, name: str, max_health: int, level: int, armor: int) -> None:
        super().__init__(name, max_health, level)
        if not isinstance(armor, int):
            raise ValueError("Armor must be an integer")
        self._armor = armor

    @property
    def armor(self) -> int:
        return self._armor

    def power_attack(self) -> str:
        return "Warrior's powerful attack!"

    def take_damage(self, damage: int) -> None:
        super().take_damage(damage - (damage * self.armor // 100))


class Mage(Character):
    def __init__(self, name: str, max_health: int, level: int, mana: int, max_mana: int) -> None:
        super().__init__(name, max_health, level)
        if not isinstance(mana, int):
            raise ValueError("Mana must be an integer")
        if not isinstance(max_mana, int):
            raise ValueError("Max Mana must be an integer")
        self._mana = mana
        self._max_mana = max_mana

    @property
    def mana(self) -> int:
        return self._mana

    @property
    def max_mana(self) -> int:
        return self._max_mana

    def get_mana(self) -> int:
        return self._mana

    def cast_spell(self, mana_cost: int) -> bool:
        if self._mana >= mana_cost and mana_cost > 0:
            self._mana -= mana_cost
            return True
        else:
            return False

    def restore_mana(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("Mana restoration amount must be a positive integer")
        if amount > self._max_mana - self._mana:
            self._mana = self._max_mana
        else:
            self._mana += amount


class Archer(Character):
    def __init__(self, name: str, max_health: int, level: int, arrows: int) -> None:
        super().__init__(name, max_health, level)
        if not isinstance(arrows, int):
            raise ValueError("Arrows must be an integer")
        self._arrows = arrows

    @property
    def arrows(self) -> int:
        return self._arrows

    def get_arrows(self) -> int:
        return self._arrows

    def shoot_arrow(self) -> bool:
        if self._arrows > 0:
            self._arrows -= 1
            return True
        else:
            return False

    def collect_arrows(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("Arrow collection amount must be a positive integer")
        if amount > self._arrows + amount:
            self._arrows += amount
        else:
            self._arrows = amount


class Item:
    def __init__(self, name: str, value: int, item_type: str) -> None:
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if not isinstance(value, int):
            raise ValueError("Value must be an integer")
        if not isinstance(item_type, str):
            raise ValueError("Item type must be a string")
        self._name = name
        self._value = value
        self._item_type = item_type

    @property
    def name(self) -> str:
        return self._name

    @property
    def value(self) -> int:
        return self._value

    @property
    def item_type(self) -> str:
        return self._item_type

    def __str__(self) -> str:
        return f"{self.name} ({self.item_type}) - {self.value} gold"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Item):
            return False
        return self._name == other._name


class Inventory:
    def __init__(self, max_capacity: int) -> None:
        if not isinstance(max_capacity, int):
            raise ValueError("Max capacity must be an integer")
        self._items = []
        self._max_capacity = max_capacity

    @property
    def items(self) -> list[Item]:
        return self._items

    @property
    def max_capacity(self) -> int:
        return self._max_capacity

    def add_item(self, item: Item) -> bool:
        if len(self.items) >= self.max_capacity:
            raise ValueError("Inventory is full")
        self.items.append(item)
        return True

    def remove_item(self, item_name: str) -> bool:
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                return True
        return False

    def get_item(self, item_name: str) -> Item | None:
        for item in self.items:
            if item.name == item_name:
                return item
        return None

    def get_total_value(self) -> int:
        total = 0
        for item in self.items:
            total += item.value
        return total

    def is_full(self) -> bool:
        return len(self.items) >= self.max_capacity

    def list_items(self) -> None:
        for item in self.items:
            print(item)

    def __str__(self) -> str:
        return f"Inventory ({self.max_capacity} capacity): {', '.join([item.name for item in self.items])}"


def battle_simulation(characters: list[Character]) -> None:
    """Simulate a battle with various character types."""
    for character in characters:
        print(character)
        character.take_damage(20)

        if isinstance(character, Warrior):
            print(character.power_attack())
        elif isinstance(character, Mage):
            character.cast_spell(10)
        elif isinstance(character, Archer):
            character.shoot_arrow()


def main() -> None:
    """Demonstrate game mechanics."""
    warrior = Warrior("Sir Galahad", 100, 1, 50)
    mage = Mage("Merlin the Wise", 80, 1, 100, 100)
    archer = Archer("Robin Hood", 90, 1, 20)

    print(f"=== Creating Characters ===")
    print(warrior)
    print(mage)
    print(archer)

    battle_simulation([warrior, mage, archer])

    inventory = Inventory(10)
    for character in [warrior, mage, archer]:
        character.inventory = inventory

    print(f"=== Adding items to character inventories ===")
    warrior.add_item(Item("Health Potion", 50, "potion"))
    mage.add_item(Item("Mana Crystal", 30, "crystal"))
    archer.add_item(Item("Arrow Pack", 20, "arrows"))

    print(f"=== Using potions to heal characters ===")
    warrior.heal(10)
    mage.heal(15)

    print(f"=== Calling battle_simulation() function ===")
    battle_simulation([warrior, mage, archer])

    if warrior == mage:
        print("Characters are the same!")
    else:
        print("Characters are different!")

    if isinstance(warrior, Character):
        print("Warrior is a character!")
    else:
        print("Warrior is not a character!")


if __name__ == "__main__":
    main()
```

