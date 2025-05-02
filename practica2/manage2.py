import random

# персонаж
class Character:
    def __init__(self, name, health, attack, defence):
        self.name = name
        self.health = health
        self.attack = attack
        self.defence = defence

    def is_alive(self):
        return self.health > 0

    def attack_target(self, other):
        damage = max(self.attack - other.defence, 0)
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона!")

# состояние персов
def print_status(hero, monster):
    print("\nСтатус:")
    print(f"{hero.name} - Здоровье: {hero.health}, Атака: {hero.attack}, Защита: {hero.defence}")
    print(f"{monster.name} - Здоровье: {monster.health}, Атака: {monster.attack}, Защита: {monster.defence}\n")

# ход player
def player_turn(hero, monster):
    while True:
        print("Твой ход:")
        print("1 - Атака")
        print("2 - Пропуск хода")
        choice = input("Выберите действие: ")
        if choice == '1':
            hero.attack_target(monster)
            break
        elif choice == '2':
            print(f"{hero.name} пропуск хода.")
            break
        else:
            print("Ошибка! Введите 1 или 2.")

# Ход monster
def monster_turn(monster, hero):
    action = random.choice(['attack', 'skip'])
    if action == 'attack':
        monster.attack_target(hero)
    else:
        print(f"{monster.name} пропуск хода.")

def game():
    print("Добро пожаловать в игру 'Битва с монстром'!")

    while True:
        hero = Character("Герой", 100, random.randint(15, 25), random.randint(5, 10))
        monster = Character("Монстр", 80, random.randint(10, 20), random.randint(3, 8))

        # бой 
        while hero.is_alive() and monster.is_alive():
            print_status(hero, monster)
            player_turn(hero, monster)
            if not monster.is_alive():
                print(f"\n{monster.name} побежден! You Win )")
                break
            monster_turn(monster, hero)
            if not hero.is_alive():
                print(f"\n{hero.name} пал в бою... You Lose (.")
                break

        again = input("Сыграть снова? (y/n): ").lower()
        if again != 'y':
            print("Спасибо за игру!")
            break

if __name__ == "__main__":
    game()
