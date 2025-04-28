import random

def play_game():
    number_to_guess = random.randint(1, 100)
    attempts_left = 10  
    attempts_used = 0

    print("'Угадай число'!")
    print("загадано число от 1 до 100. угадай его!")

    while attempts_left > 0:
        try:
            guess = int(input("Пиши число: "))
            
            if guess < 1 or guess > 100:
                print("Ошибка: введите число от 1 до 100.")
                continue
        except ValueError:
            print("Ошибка: введите число подходящие параметрам.")
            continue

        attempts_used += 1
        attempts_left -= 1

        if guess < number_to_guess:
            print("Загаданное число больше.")
        elif guess > number_to_guess:
            print("Загаданное число меньше.")
        else:
            print(f"Красава! угадал число {number_to_guess} за {attempts_used} попыток.")
            break
    else:
        print(f"ПОТРАЧЕНО {number_to_guess}.")

def main():
    while True:
        play_game()
        play_again = input("сыграть ещё раз? (да/нет): ").strip().lower()
        if play_again != 'да':
            print("СПС за игру !")
            break

if __name__ == "__main__":
    main()
