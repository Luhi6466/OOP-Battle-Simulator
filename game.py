from goblin import Goblin
from hero import Hero

ARENA_NAME = "room 212"

def battle(hero: Hero, enemy: Goblin):
    while hero.is_alive() and enemy.is_alive():
        hero_damage = hero.attack()
        enemy.take_damage(hero_damage)

        if enemy.is_alive():
            enemy_damage = enemy.attack()
            hero.take_damage(enemy_damage)
    if hero.is_alive():
        print(f"{hero.name} WINS!")
    else:
        print(f"{enemy.name} WINS!")


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
    cry = hero.battle_cry()
    battle(hero, gooblin)
    
    
if __name__ == "__main__":
    main()
