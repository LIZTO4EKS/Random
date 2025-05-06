import pygame
import random
import os
import time

pygame.init()

#окно на весь экран
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width, screen_height = screen.get_size()  # Получаем размер экрана
pygame.display.set_caption("Поймай Призрака!")

font = pygame.font.SysFont(None, int(screen_height // 20))  # Шрифт с размером, зависящим от высоты экрана
clock = pygame.time.Clock()

# Загрузка анимации
ghost_frames = []
ghost_folder = "image"
for i in range(1, 7):
    img = pygame.image.load(os.path.join(ghost_folder, f"ghost{i}.png")).convert_alpha()
    img = pygame.transform.scale(img, (int(screen_height // 10), int(screen_height // 10)))  # Пропорциональный размер
    ghost_frames.append(img)

frame_index = 0
animation_timer = 0
animation_speed = 100  


score = 0
game_time = 30
ghost_timer = 0
ghost_delay = random.randint(1000, 2000)
ghost_visible = False
ghost_duration = 700
ghost_rect = pygame.Rect(0, 0, 0, 0)

start_ticks = pygame.time.get_ticks()
game_over = False

def show_text(text, pos, color=(255, 255, 255)):
    img = font.render(text, True, color)
    screen.blit(img, pos)

def reset_game():
    global score, start_ticks, game_over
    score = 0
    start_ticks = pygame.time.get_ticks()
    game_over = False

#загрузка
def loading_screen():
    loading_font = pygame.font.SysFont(None, int(screen_height // 10)) 
    screen.fill((0, 0, 0))  # чёрный фон
    show_text("Загрузка...", (screen_width // 3, screen_height // 2), (255, 255, 255))

    pygame.draw.rect(screen, (255, 0, 0), (screen_width // 4, screen_height // 2 + int(screen_height // 10), screen_width // 2, 50))
    pygame.draw.rect(screen, (0, 255, 0), (screen_width // 4, screen_height // 2 + int(screen_height // 10), screen_width // 4, 50))

    pygame.display.flip()
    time.sleep(2) 

# запуск игры
loading_screen()

running = True
while running:
    dt = clock.tick(60)
    current_ticks = pygame.time.get_ticks()
    screen.fill((30, 30, 60))

    seconds = game_time - (current_ticks - start_ticks) // 1000
    if seconds <= 0:
        game_over = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            if ghost_visible and ghost_rect.collidepoint(event.pos):
                score += 1
                ghost_visible = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and game_over:
            reset_game()

    if not ghost_visible and not game_over and current_ticks - ghost_timer > ghost_delay:
        ghost_x = random.randint(int(screen_width // 5), int(screen_width * 0.7))
        ghost_y = random.randint(int(screen_height // 5), int(screen_height * 0.7))
        ghost_rect = pygame.Rect(ghost_x, ghost_y, int(screen_height // 10), int(screen_height // 10)) 
        ghost_timer = current_ticks
        ghost_visible = True
        ghost_delay = random.randint(1000, 2000)

    if ghost_visible:
        animation_timer += dt
        if animation_timer >= animation_speed:
            frame_index = (frame_index + 1) % len(ghost_frames)
            animation_timer = 0
        screen.blit(ghost_frames[frame_index], ghost_rect.topleft)
        if current_ticks - ghost_timer >= ghost_duration:
            ghost_visible = False

    show_text("Счёт: " + str(score), (screen_width * 0.02, screen_height * 0.02))
    show_text("Время: " + str(seconds), (screen_width * 0.8, screen_height * 0.02))
    show_text("Кликай по призраку, пока не закончится время!", (screen_width // 3, screen_height * 0.9))

    if game_over:
        show_text(f"Время вышло! Ваш счёт: {score}. Нажмите ПРОБЕЛ, чтобы начать заново.", (screen_width // 4, screen_height // 2), (255, 200, 200))

    pygame.display.flip()

pygame.quit()
