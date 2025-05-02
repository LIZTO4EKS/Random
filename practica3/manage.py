import random

# Класс игрока
class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.health = 100

    def move(self, direction, size):
        dx, dy = 0, 0
        if direction == 'w': dx = -1
        elif direction == 's': dx = 1
        elif direction == 'a': dy = -1
        elif direction == 'd': dy = 1

        new_x = self.x + dx
        new_y = self.y + dy

        if 0 <= new_x < size and 0 <= new_y < size:
            self.x, self.y = new_x, new_y
            return True
        else:
            print("Нельзя выйти за границы поля!")
            return False

# Функция генерации поля
def generate_field(size, traps_count):
    field = [['.' for _ in range(size)] for _ in range(size)]
    
    # Размещение ловушек
    trap_positions = random.sample([(i, j) for i in range(size) for j in range(size) if (i, j) != (0, 0)], traps_count)
    for x, y in trap_positions:
        field[x][y] = 'T'
    
    # Размещение выхода
    while True:
        exit_x, exit_y = random.randint(0, size-1), random.randint(0, size-1)
        if field[exit_x][exit_y] == '.' and (exit_x, exit_y) != (0, 0):
            field[exit_x][exit_y] = 'X'
            break

    return field

# Вывод поля
def print_field(field, player):
    size = len(field)
    for i in range(size):
        row = ''
        for j in range(size):
            if i == player.x and j == player.y:
                row += 'P '
            else:
                row += field[i][j] + ' '
        print(row.strip())
    print()

# Основной игровой цикл
def play_game():
    size = 5
    traps = random.randint(3, 5)
    field = generate_field(size, traps)
    player = Player()

    while True:
        print_field(field, player)
        print(f"Здоровье: {player.health}")
        move = input("Двигаться (w/a/s/d): ").lower()

        if move not in ['w', 'a', 's', 'd']:
            print("Неверная команда. Используй w, a, s, d.")
            continue

        moved = player.move(move, size)
        if not moved:
            continue

        cell = field[player.x][player.y]
        if cell == 'T':
            player.health -= 20
            print("Ловушка! -20 HP.")
            field[player.x][player.y] = '.'
        elif cell == 'X':
            print_field(field, player)
            print("Ты нашёл выход! Победа!")
            break

        if player.health <= 0:
            print_field(field, player)
            print("Ты погиб в лабиринте... Поражение.")
            break

    again = input("Сыграть снова? (y/n): ").lower()
    if again == 'y':
        play_game()
    else:
        print("Выход из игры.")

# Запуск игры
play_game()
