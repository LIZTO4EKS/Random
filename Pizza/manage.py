import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размеры экрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Заказ пиццы и напитков")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Шрифт
font = pygame.font.Font(None, 36)

# Состояния экрана
MENU = "menu"
PIZZA_MENU = "pizza_menu"
DRINK_MENU = "drink_menu"
PIZZA_CONFIRMATION = "pizza_confirmation"
DRINK_CONFIRMATION = "drink_confirmation"
ORDER_STATUS = "order_status"

# Текущее состояние
state = MENU

# Заказ
order = []

# Кнопка
class Button:
    def __init__(self, rect, color, text, action=None):
        self.rect = pygame.Rect(rect)
        self.color = color
        self.text = text
        self.action = action

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surf = font.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Кнопки главного меню
main_menu_buttons = [
    Button((300, 200, 200, 50), GRAY, "Пицца", lambda: change_state(PIZZA_MENU)),
    Button((300, 300, 200, 50), GRAY, "Напитки", lambda: change_state(DRINK_MENU)),
    Button((300, 400, 200, 50), GRAY, "Мой заказ", lambda: change_state(ORDER_STATUS)),
]

# Кнопки выбора пиццы
pizza_buttons = [
    Button((100, 150, 250, 50), GRAY, "Пицца Маргарита", lambda: confirm_item("Пицца Маргарита", PIZZA_CONFIRMATION)),
    Button((100, 220, 250, 50), GRAY, "Пицца Пепперони", lambda: confirm_item("Пицца Пепперони", PIZZA_CONFIRMATION)),
    Button((100, 290, 250, 50), GRAY, "Пицца Четыре сыра", lambda: confirm_item("Пицца Четыре сыра", PIZZA_CONFIRMATION)),
    Button((600, 500, 150, 50), GRAY, "Назад", lambda: change_state(MENU))
]

# Кнопки выбора напитков
drink_buttons = [
    Button((100, 150, 250, 50), GRAY, "Кола", lambda: confirm_item("Кола", DRINK_CONFIRMATION)),
    Button((100, 220, 250, 50), GRAY, "Сок", lambda: confirm_item("Сок", DRINK_CONFIRMATION)),
    Button((100, 290, 250, 50), GRAY, "Вода", lambda: confirm_item("Вода", DRINK_CONFIRMATION)),
    Button((600, 500, 150, 50), GRAY, "Назад", lambda: change_state(MENU))
]

# Кнопки подтверждения заказа
confirmation_buttons = [
    Button((200, 400, 150, 50), GRAY, "Подтвердить", lambda: add_to_order()),
    Button((450, 400, 150, 50), GRAY, "Отмена", lambda: go_back())
]

# Кнопки статуса заказа
order_buttons = [
    Button((600, 500, 150, 50), GRAY, "Назад", lambda: change_state(MENU))
]

# Переменная для хранения выбранного элемента
selected_item = ""

# Изменение состояния
def change_state(new_state):
    global state
    state = new_state

# Подтверждение выбора элемента
def confirm_item(item, next_state):
    global selected_item, state
    selected_item = item
    state = next_state

# Добавление в заказ
def add_to_order():
    global selected_item, state
    order.append(selected_item)
    selected_item = ""
    state = MENU

# Вернуться назад без добавления
def go_back():
    global selected_item, state
    selected_item = ""
    state = PIZZA_MENU if state == PIZZA_CONFIRMATION else DRINK_MENU

# Отрисовка кнопок
def draw_buttons(buttons):
    screen.fill(WHITE)
    for button in buttons:
        button.draw(screen)
    pygame.display.flip()

# Главный цикл
running = True
while running:
    # Отрисовка кнопок, если не отображается отдельный экран подтверждения или заказ
    if state not in [PIZZA_CONFIRMATION, DRINK_CONFIRMATION, ORDER_STATUS]:
        if state == MENU:
            buttons = main_menu_buttons
        elif state == PIZZA_MENU:
            buttons = pizza_buttons
        elif state == DRINK_MENU:
            buttons = drink_buttons
        else:
            buttons = []
        draw_buttons(buttons)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            if state == PIZZA_CONFIRMATION or state == DRINK_CONFIRMATION:
                for button in confirmation_buttons:
                    if button.is_clicked(pos):
                        button.action()
            elif state == ORDER_STATUS:
                for button in order_buttons:
                    if button.is_clicked(pos):
                        button.action()
            else:
                for button in buttons:
                    if button.is_clicked(pos):
                        button.action()

    # Показываем подтверждение выбора пиццы или напитка
    if state in [PIZZA_CONFIRMATION, DRINK_CONFIRMATION]:
        screen.fill(WHITE)
        text = font.render(f"Добавить в заказ: {selected_item}?", True, BLACK)
        screen.blit(text, (250, 250))
        for button in confirmation_buttons:
            button.draw(screen)
        pygame.display.flip()

    # Показываем текущий заказ
    elif state == ORDER_STATUS:
        screen.fill(WHITE)
        y = 100
        screen.blit(font.render("Ваш заказ:", True, BLACK), (50, 50))
        for item in order:
            screen.blit(font.render(f"- {item}", True, BLACK), (50, y))
            y += 40
        for button in order_buttons:
            button.draw(screen)
        pygame.display.flip()

# Завершение работы
pygame.quit()
sys.exit()
