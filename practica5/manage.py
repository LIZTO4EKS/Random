import pygame
import random
import sys

pygame.init()

# само окно 
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("✊, ✌️, ✋")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# наш шрифт можно и без него 
font = pygame.font.SysFont(None, 40)

player_choice = ""
computer_choice = ""
result = ""
game_active = True
clock = pygame.time.Clock()

def draw_text(text, x, y, color=BLACK):
    render = font.render(text, True, color)
    screen.blit(render, (x, y))

def get_result(player, computer):
    if player == computer:
        return "Ничья!"
    elif (player == "Камень" and computer == "Ножницы") or \
         (player == "Ножницы" and computer == "Бумага") or \
         (player == "Бумага" and computer == "Камень"):
        return "Вы выиграли!"
    else:
        return "Вы проиграли!"

# гланый цикл отвечающий за кнопки их действия и происходящие на экране
running = True
while running:
    screen.fill(WHITE)

    draw_text("Камень, Ножницы, Бумага", 250, 50)
    draw_text("Нажмите Q для Камня", 100, 150)
    draw_text("Нажмите W для Бумаги", 100, 200)
    draw_text("Нажмите E для Ножниц", 100, 250)

    if player_choice:
        draw_text(f"Вы выбрали: {player_choice}", 100, 350)
        draw_text(f"Компьютер выбрал: {computer_choice}", 100, 400)
        draw_text(result, 100, 450)
        draw_text("Нажмите ПРОБЕЛ, чтобы сыграть снова", 100, 500)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if game_active:
                if event.key == pygame.K_q:
                    player_choice = "Камень"
                elif event.key == pygame.K_w:
                    player_choice = "Бумага"
                elif event.key == pygame.K_e:
                    player_choice = "Ножницы"

                if player_choice:
                    computer_choice = random.choice(["Камень", "Бумага", "Ножницы"])
                    result = get_result(player_choice, computer_choice)
                    game_active = False

            elif event.key == pygame.K_SPACE:
                player_choice = ""
                computer_choice = ""
                result = ""
                game_active = True

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
