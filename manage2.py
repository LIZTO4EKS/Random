import random

try:
    # Для цветного текста в концоли нашел идею в ChatGPT ! 
    from colorama import init, Fore, Style
    init(autoreset=True)
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False

def initialize_data():
    heroes = [
        "Евгений Александрович",
        "Даниярбет Казымбетович",
        "Молния Маквин",
        "Толкачев Иван",
        "Сын маминой подруги"
    ]
    places = [
        "в Павлодаре",
        "на Максима Горького 102/2",
        "в густом Мичуринском лесу",
        "на просторах ПВЕКК",
        "у подножия 2-го корпуса"
    ]
    events = [
        "победил Папа",
        "обнаружил 1000 тенге в куртке",
        "выиграл катку",
        "устроил запой",
        "раскрыл тайну"
    ]
    details = [
        "с волшебным заявлением",
        "на летающем слоне",
        "под звуки спящего деда",
        "с удивительной рожей",
        "в сопровождении Мексиканского картеля"
    ]
    return heroes, places, events, details

def generate_story(heroes, places, events, details):
    hero = random.choice(heroes)
    place = random.choice(places)
    event = random.choice(events)
    detail = random.choice(details)
    story = f"{hero} {place} {event} {detail}."
    return story

def save_story(story):
    try:
        with open("stories.txt", "a", encoding="utf-8") as file:
            file.write(story + "\n")
        print(Fore.GREEN + "История успешно сохранена в файл!" if COLORAMA_AVAILABLE else "История успешно сохранена в файл!")
    except IOError:
        print(Fore.RED + "Ошибка при записи в файл." if COLORAMA_AVAILABLE else "Ошибка при записи в файл.")

def ask_play_again():
    answer = input("\nХотите создать новую историю? (да/нет): ").strip().lower()
    return answer == "да"

def decorate_story(story):
    line = "-" * (len(story) + 4)
    decorated = f"\n{line}\n| {story} |\n{line}\n"
    if COLORAMA_AVAILABLE:
        return Fore.CYAN + decorated
    else:
        return decorated

def main():
    heroes, places, events, details = initialize_data()
    
    print("Добро пожаловать в Генератор Историй!")
    
    while True:
        story = generate_story(heroes, places, events, details)
        print(decorate_story(story))
        
        save = input("\nХотите сохранить эту историю в файл? (да/нет): ").strip().lower()
        if save == "да":
            save_story(story)
        
        if not ask_play_again():
            print("\nСпасибо за игру! До свидания!")
            break

if __name__ == "__main__":
    main()
