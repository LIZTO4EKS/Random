import os

def print_field(field):
    print()
    print(f" {field[0]} | {field[1]} | {field[2]}")
    print("-----------")
    print(f" {field[3]} | {field[4]} | {field[5]}")
    print("-----------")
    print(f" {field[6]} | {field[7]} | {field[8]}")
    print()

def check_win(field, symbol):
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  
        (0, 4, 8), (2, 4, 6)             
    ]
    return any(field[a] == field[b] == field[c] == symbol for a, b, c in win_combinations)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_game():
    while True:
        field = [str(i) for i in range(1, 10)]
        current_player = 'X'
        move_count = 0

        while True:
            clear_console()
            print_field(field)

            move = input(f"{current_player}, выбери ячейку (1–9): ")

            if not move.isdigit() or not (1 <= int(move) <= 9):
                print("Неверный ввод. Введите число от 1 до 9.")
                input("Нажмите Enter, чтобы продолжить...")
                continue

            move = int(move) - 1
            if field[move] in ['X', 'O']:
                print("Клетка уже занята. Выберите другую.")
                input("Нажмите Enter, чтобы продолжить...")
                continue

            field[move] = current_player
            move_count += 1

            if check_win(field, current_player):
                clear_console()
                print_field(field)
                print(f"Игрок {current_player} победил!🎉🎉 ")
                break

            if move_count == 9:
                clear_console()
                print_field(field)
                print("Ничья! 🤡")
                break

            current_player = 'O' if current_player == 'X' else 'X'

        again = input("По новой ?? (Go/No ): ").strip().lower()
        if again != 'Go':
            print("Спасибо за игру! 👋 ")
            break

play_game()
