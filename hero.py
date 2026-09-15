import random

class Hero:
    """A playable character who battles enemies in the arena"""

    def __init__(self, name):
        self.name = name
        self.health = 125
        self.attack_power = 20

    def attack(self):
        return random.randint(1, self.attack_power)

    def battle_cry(self):
        self.cry = "I'll get ya"
        print(f"{self.name} yells: {self.cry}")

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def is_alive(self):
            return self.health > 0