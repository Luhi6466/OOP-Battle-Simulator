from goblin import Goblin
from hero import Hero

ARENA_NAME = "room 212"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Gribble")
    gooblin = Goblin("Nibble")
    hero = Hero("Justin")
    
    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print(f"{gooblin.name} enters the arena with {goblin.health} health.")
    print(f"{hero.name}  enters the arena with {hero.health} health.")
    print(hero.battle_cry)

    print(f"{hero.name} attacks {gooblin.name}.")
    attack = hero.attack()
    gooblin.take_damage(attack)
    print(f"{gooblin.name} fights back.")
    g2attack = gooblin.attack()
    hero.take_damage(g2attack)
    
    
if __name__ == "__main__":
    main()
